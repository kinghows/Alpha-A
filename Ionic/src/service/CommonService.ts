import {Injectable} from '@angular/core';
import {Observable} from "rxjs";
import {Response} from "@angular/http";
import {HttpService} from "../providers/HttpService";
/**
 *
 */
@Injectable()
export class CommonService {
  constructor(public httpService: HttpService) {
  }


  /**
   * 查询公告列表
   * @returns {Observable<R>}
   */
  findPublishList() {
    return this.httpService.post('/sys/notice/findPublishList').map((res: Response) => res.json());
  }

  /**
   * 查询公告详情
   * @returns {Observable<R>}
   */
  getPublishDetail(id) {
    return this.httpService.get(`/sys/notice/getById/${id}`).map((res: Response) => res.json());
  }
  //获取新token
  getNewToken(sessiontoken) {
    // return this.httpService.post('/sessiontoken', sessiontoken).map((res: Response) => res.json());
    return Observable.create((observer) => {
      observer.next({logintoken: 'OLANLF',sessiontoken: 'OLANLF'});
    });
  }


  //更新文件缓存文件关系
  fileRelationReplace(data) {
    return this.httpService.post('/fileRelation/replace', data).map((res: Response) => res.json());
  }

}
