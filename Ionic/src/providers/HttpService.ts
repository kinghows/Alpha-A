import {Injectable} from '@angular/core';
import {
  Http, Response, Headers, RequestOptions, URLSearchParams, RequestOptionsArgs, RequestMethod
} from '@angular/http';
import 'rxjs/add/operator/toPromise';
import {Observable, TimeoutError} from "rxjs";
import {Utils} from "./Utils";
import {GlobalData} from "./GlobalData";
import {NativeService} from "./NativeService";
import {APP_SERVE_URL, REQUEST_TIMEOUT, IS_DEBUG} from "./Constants";
import {Logger} from "./Logger";



@Injectable()
export class HttpService {
  myInfoLocal: any;
  local: Storage;
  constructor(public http: Http,
              private globalData: GlobalData,
              public logger: Logger,
              private nativeService: NativeService) {
  }
    
  public request(url: string, options: RequestOptionsArgs): Observable<Response> {
    url = Utils.formatUrl(url.startsWith('http') ? url : APP_SERVE_URL + url);
    this.optionsAddToken(options);
    return Observable.create(observer => {
      this.nativeService.showLoading();
      IS_DEBUG && console.log('%c 请求前 %c', 'color:blue', '', 'url', url, 'options', options);
      this.http.request(url, options).timeout(REQUEST_TIMEOUT).subscribe(res => {
        this.nativeService.hideLoading();
        IS_DEBUG && console.log('%c 请求成功 %c', 'color:green', '', 'url', url, 'options', options, 'res', res);
        if (res['_body'] == '') {
          res['_body'] = null;
        }
        observer.next(res);
      }, err => {
        this.requestFailed(url, options, err);//处理请求失败
        observer.error(err);
      });
    });
  }

  public get(url: string, paramMap: any = null): Observable<Response> {
    return this.request(url, new RequestOptions({
      method: RequestMethod.Get,
      search: HttpService.buildURLSearchParams(paramMap)
    }));
  }

  public post(url: string, body: any = {}): Observable<Response> {
    return this.request(url, new RequestOptions({
      method: RequestMethod.Post,
      body: body,
      headers: new Headers({
        'Content-Type': 'application/json; charset=UTF-8'
      })
    }));
  }
    
  public postFormData(url: string, paramMap: any = null): Observable<Response> {
    return this.request(url, new RequestOptions({
      method: RequestMethod.Post,
      search: HttpService.buildURLSearchParams(paramMap).toString(),
      headers: new Headers({
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
      })
    }));
  }

  public put(url: string, body: any = {}): Observable<Response> {
    return this.request(url, new RequestOptions({
      method: RequestMethod.Put,
      body: body
    }));
  }

  public delete(url: string, paramMap: any = null): Observable<Response> {
    return this.request(url, new RequestOptions({
      method: RequestMethod.Delete,
      search: HttpService.buildURLSearchParams(paramMap).toString()
    }));
  }

  public patch(url: string, body: any = {}): Observable<Response> {
    return this.request(url, new RequestOptions({
      method: RequestMethod.Patch,
      body: body
    }));
  }
    
  public head(url: string, paramMap: any = null): Observable<Response> {
    return this.request(url, new RequestOptions({
      method: RequestMethod.Head,
      search: HttpService.buildURLSearchParams(paramMap).toString()
    }));
  }

  public options(url: string, paramMap: any = null): Observable<Response> {
    return this.request(url, new RequestOptions({
      method: RequestMethod.Options,
      search: HttpService.buildURLSearchParams(paramMap).toString()
    }));
  }

  /**
   * 将对象转为查询参数
   * @param paramMap
   * @returns {URLSearchParams}
   */
  private static buildURLSearchParams(paramMap): URLSearchParams {
    let params = new URLSearchParams();
    if (!paramMap) {
      return params;
    }
    for (let key in paramMap) {
      let val = paramMap[key];
      if (val instanceof Date) {
        val = Utils.dateFormat(val, 'yyyy-MM-dd hh:mm:ss')
      }
      params.set(key, val);
    }
    return params;
  }

  /**
   * 处理请求失败事件
   * @param url
   * @param options
   * @param err
   */
  private requestFailed(url: string, options: RequestOptionsArgs, err: Response): void {
    this.nativeService.hideLoading();
    IS_DEBUG && console.log('%c 请求失败 %c', 'color:red', '', 'url', url, 'options', options, 'err', err);
    if (err instanceof TimeoutError) {
      this.nativeService.alert('请求超时,请稍后再试!');
      return;
    }
    //err数据类型不确定,判断消息体是否有message字段,如果有说明是后台返回的json数据
    let index = JSON.stringify(err['_body']).indexOf('message');
    if (index != -1) {
      this.nativeService.alert(err.json().message || '请求发生异常');
      return;
    }
    if (!this.nativeService.isConnecting()) {
      this.nativeService.alert('请连接网络');
      return;
    }
    let status = err.status;
    let msg = '请求发生异常';
    if (status === 0) {
      msg = '请求失败，请求响应出错!!!';
    } else if (status === 404) {
      msg = '请求失败，未找到请求地址';
    } else if (status === 500) {
      msg = '请求失败，服务器出错，请稍后再试';
    }
    this.nativeService.alert(msg);
    this.logger.httpLog(err, msg, {
      url: url,
      status: status
    });
  }

  private optionsAddToken(options: RequestOptionsArgs): void {
    let logintoken = this.globalData.logintoken;
    if (options.headers) {
      options.headers.append('Authorization', 'logintoken ' + logintoken);
    } else {
      options.headers = new Headers({
        'Authorization': 'logintoken ' + logintoken
      });
    }
  }
  

}
//传中文时需要做一下处理，不然会出现被转码，应该是这样吧
//class MyQueryEncoder extends QueryEncoder {
//  encodeKey(k: string): string {
//    return k;
//  }
//
//  encodeValue(v: string): string {
//    return v;
//  }
//}