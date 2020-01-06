import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';
import { Http, Response } from '@angular/http';

@Component({
  selector: 'page-msg',
  templateUrl: 'msg.html'
})
export class msgPage {
  listData: Object;

  constructor(public navCtrl: NavController, private http: Http) {

  }

  ionViewDidLoad() {
    this.http.request('http://221.133.231.70:9000/today_stock')
    .subscribe((res: Response) => {
      this.listData = res.json();
    });
  }
}
