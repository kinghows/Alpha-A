import { Component } from '@angular/core';
import {NavController, Events} from 'ionic-angular';

import { msgPage } from '../msg/msg';
import { poolPage } from '../pool/pool';
import { indexPage } from '../index/index';
import { alphaPage } from '../alpha/alpha';


@Component({
  templateUrl: 'tabs.html'
})
export class TabsPage {

  tab1Root = indexPage;
  tab2Root = msgPage;
  tab3Root = poolPage;
  tab4Root = alphaPage;

  
  constructor(private nav: NavController, private events: Events) {
  }

  ionViewDidLoad() {
    this.listenEvents();
    // console.log('界面创建');
  }

  ionViewWillUnload() {
    this.events.unsubscribe('indexPage');
    // console.log('界面销毁');
  }

  listenEvents() {
    this.events.subscribe('indexPage', () => {
      this.nav.setRoot(indexPage);
      // this.nav.pop(); 使用这种方式也可以，但是会在登录框中默认填上值
      // console.log('返回登录');
    });
  }
}
