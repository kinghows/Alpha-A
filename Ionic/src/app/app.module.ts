import { NgModule, ErrorHandler } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { IonicApp, IonicModule,IonicErrorHandler, Config } from 'ionic-angular';
import { AlphaA } from './app.component';
import { HttpModule } from '@angular/http';

import {IonicStorageModule} from "@ionic/storage";
import {JPush} from "../../typings/modules/jpush/index";
import {AppVersion} from "@ionic-native/app-version";
import {Camera} from "@ionic-native/camera";
import {Toast} from "@ionic-native/toast";
import {File} from "@ionic-native/file";
import {FileTransfer} from "@ionic-native/file-transfer";
import {InAppBrowser} from "@ionic-native/in-app-browser";
import {ImagePicker} from "@ionic-native/image-picker";
import {Network} from "@ionic-native/network";
import {AppMinimize} from "@ionic-native/app-minimize";
import {CallNumber} from "@ionic-native/call-number";
import {BarcodeScanner} from "@ionic-native/barcode-scanner";
import {Diagnostic} from "@ionic-native/diagnostic";
import {CodePush} from "@ionic-native/code-push";

import { msgPage } from '../pages/msg/msg';
import { indexPage } from '../pages/index/index';
import { TabsPage } from '../pages/tabs/tabs';
import { poolPage } from '../pages/pool/pool';
import { alphaPage } from '../pages/alpha/alpha';
import {GlobalData} from "../providers/GlobalData";
import {NativeService} from "../providers/NativeService";
import {HttpService} from "../providers/HttpService";
import {FileService} from "../providers/FileService";
import {Helper} from "../providers/Helper";
import {Utils} from "../providers/Utils";
import {Logger} from "../providers/Logger";

import { StatusBar } from '@ionic-native/status-bar';
import { SplashScreen } from '@ionic-native/splash-screen';

import { ProgressBarComponent } from '../components/progress-bar/progress-bar';
import {CommonService} from "../service/CommonService";
import {ModalFromRightEnter, ModalFromRightLeave, ModalScaleEnter, ModalScaleLeave} from "./modal-transitions";


@NgModule({
  declarations: [
    AlphaA,
	indexPage,
    msgPage,
    poolPage,
	alphaPage,
    TabsPage,
    ProgressBarComponent
  ],
  imports: [
    BrowserModule,
	HttpModule,
    IonicStorageModule.forRoot(),
    IonicModule.forRoot(AlphaA)
    //IonicPageModule.forRoot(AlphaA)   
  ],
  bootstrap: [IonicApp],
  entryComponents: [
    AlphaA,
	indexPage,
    msgPage,
    poolPage,
	alphaPage,
    TabsPage,
  ],
  providers: [
    StatusBar,
    SplashScreen,
    JPush,
    AppVersion,
    Camera,
    Toast,
    File,
    FileTransfer,
    InAppBrowser,
    ImagePicker,
    Network,
    AppMinimize,
    CallNumber,
    BarcodeScanner,
    Diagnostic,
    CodePush,
    NativeService,
    HttpService,
    FileService,
    Helper,
    Utils,
    GlobalData,
    Logger,
    CommonService,
    {provide: ErrorHandler, useClass: IonicErrorHandler}
  ]
})
export class AppModule {
  constructor(public config: Config) {
    this.setCustomTransitions();
  }

  private setCustomTransitions() {
    this.config.setTransition('modal-from-right-enter', ModalFromRightEnter);
    this.config.setTransition('modal-from-right-leave', ModalFromRightLeave);
    this.config.setTransition('modal-scale-enter', ModalScaleEnter);
    this.config.setTransition('modal-scale-leave', ModalScaleLeave);
  }
}