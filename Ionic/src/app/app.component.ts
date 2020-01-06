import { Component, ViewChild } from '@angular/core';
import { Platform, IonicApp, Nav,Keyboard, ToastController } from 'ionic-angular';
import { StatusBar } from '@ionic-native/status-bar';
import { SplashScreen } from '@ionic-native/splash-screen';
import { TabsPage } from '../pages/tabs/tabs';
import {Utils} from "../providers/Utils";
import {NativeService} from "../providers/NativeService";
import {Helper} from "../providers/Helper";
import * as fundebug from "fundebug-javascript";
//import {NavController} from "ionic-angular";

@Component({
  templateUrl: 'app.html'
})
export class AlphaA {
  @ViewChild('myNav') nav: Nav;
  rootPage:any = TabsPage;
  backButtonPressed: boolean = false;
    
  constructor(//public navCtrl: NavController,
            statusBar: StatusBar, 
            splashScreen: SplashScreen,
            private platform: Platform, 
            private keyboard: Keyboard,
            private ionicApp: IonicApp,
            private nativeService: NativeService,
            private toastCtrl: ToastController,
            private helper: Helper) {
    platform.ready().then(() => {
      // Okay, so the platform is ready and our plugins are available.
      // Here you can do any higher level native things you might need.
      
      //statusBar.styleDefault();
      //splashScreen.hide();
      if (this.nativeService.isMobile()) {//设置日志监控app的版本号
        this.nativeService.getVersionNumber().subscribe(version => {
          fundebug.appversion = version;
        })
      }
      
      this.nativeService.statusBarStyle();
      this.nativeService.splashScreenHide();
      this.registerBackButtonAction();//注册返回按键事件
      this.assertNetwork();//检测网络
      setTimeout(() => {
        this.helper.assertUpgrade().subscribe(res => {//检测app是否升级
          res.update && this.nativeService.downloadApp();
        });
        this.nativeService.sync();//启动app检查热更新
        Utils.sessionStorageClear();//清除数据缓存
      }, 10000);

    });
  }
  assertNetwork() {
    if (!this.nativeService.isConnecting()) {
      this.toastCtrl.create({
        message: '未检测到网络,请连接网络',
        showCloseButton: true,
        closeButtonText: '确定'
      }).present();
    }
  }

  registerBackButtonAction() {
    if (!this.nativeService.isAndroid()) {
      return;
    }
    this.platform.registerBackButtonAction(() => {
      if (this.keyboard.isOpen()) {//如果键盘开启则隐藏键盘
        this.keyboard.close();
        return;
      }
      //如果想点击返回按钮隐藏toast或loading或Overlay就把下面加上
      // this.ionicApp._toastPortal.getActive() ||this.ionicApp._loadingPortal.getActive()|| this.ionicApp._overlayPortal.getActive()
      let activePortal = this.ionicApp._modalPortal.getActive() || this.ionicApp._toastPortal.getActive() || this.ionicApp._overlayPortal.getActive();
      if (activePortal) {
        activePortal.dismiss();
        return;
      }
      let activeVC = this.nav.getActive();
      let tabs = activeVC.instance.tabs;
      let activeNav = tabs.getSelected();
      return activeNav.canGoBack() ? activeNav.pop() : this.nativeService.minimize();//this.showExit()

    }, 1);
  }

    
  //双击退出提示框
 // showExit() {
 //   if (this.backButtonPressed) { //当触发标志为true时，即2秒内双击返回按键则退出APP
 //     this.platform.exitApp();
 //   } else {
  //    this.nativeService.showToast('再按一次退出应用');
 //     this.backButtonPressed = true;
 //     setTimeout(() => { //2秒内没有再次点击返回则将触发标志标记为false
 //       this.backButtonPressed = false;
 //     }, 2000)
 //   }
// }


}
