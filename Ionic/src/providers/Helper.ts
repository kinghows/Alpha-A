import {Injectable} from "@angular/core";
import {NativeService} from "./NativeService";
import {Observable} from "rxjs";
import {APP_VERSION_SERVE_URL} from "./Constants";
import {Http, Response} from "@angular/http";
import {Utils} from "./Utils";
import {Logger} from "./Logger";
import {AlertController} from "ionic-angular";

/**
 * Helper类存放和业务有关的公共方法
 * @description
 */
@Injectable()
export class Helper {

  constructor(
              private http: Http,
              public logger: Logger,
              private alertCtrl: AlertController,
              private nativeService: NativeService) {
  }

  /**
   * 断言app是否需要更新
   * @returns {any}
   */
  assertUpgrade(): Observable<any> {
    if (!this.nativeService.isMobile()) {
      return Observable.of({update: false, msg: '请使用真机调试'});
    }
    return Observable.create(observer => {
      this.nativeService.getPackageName().subscribe(packageName => {//获得app包名
        let appName = packageName.substring(packageName.lastIndexOf('.') + 1);
        let appType = this.nativeService.isAndroid() ? 'android' : 'ios';
        let url = Utils.formatUrl(`${APP_VERSION_SERVE_URL}/app/${appName}/${appType}/latest/version`);
        this.http.get(url).map((res: Response) => res.json()).subscribe(res => {//从后台查询app最新版本信息
          if (!res) {
            observer.next({update: false, msg: '暂无更新信息'});
            return;
          }
          this.nativeService.getVersionNumber().subscribe(currentNo => {//获得当前app版本
            if (currentNo == res.version) {//比较版本号
              observer.next({update: false, msg: '已经是最新版本'});
            } else {
              if (res.isForcedUpdate == 1) {//判断是否强制更新
                this.alertCtrl.create({
                  title: '重要升级',
                  subTitle: '您必须升级后才能使用！',
                  enableBackdropDismiss: false,
                  buttons: [{
                    text: '确定', handler: () => {
                      observer.next({update: true, msg: ''});
                    }
                  }
                  ]
                }).present();
              } else {
                this.alertCtrl.create({
                  title: '升级',
                  subTitle: '发现新版本,是否立即升级？',
                  enableBackdropDismiss: false,
                  buttons: [
                    {
                      text: '取消', handler: () => {
                      observer.next({update: false, msg: ''});
                    }
                    },
                    {
                      text: '确定', handler: () => {
                      observer.next({update: true, msg: ''});
                    }
                    }
                  ]
                }).present();
              }
            }
          })
        }, err => {
          this.logger.log(err, '从版本升级服务获取版本信息失败', {
            url: url
          })
        })
      })
    });


  }


}
