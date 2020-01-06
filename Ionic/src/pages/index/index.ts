import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';
import { Http, Response } from '@angular/http';

@Component({
  selector: 'page-index',
  templateUrl: 'index.html'
})
export class indexPage {
  listData1: Object;
  listData2: Object;
  listData3: Object;
  listData4: Object;
  listData5: Object;
  constructor(public navCtrl: NavController, private http: Http) {

  }
  
  ionViewDidLoad() {
    this.http.request('http://221.133.231.70:9000/stockindex')
    .subscribe((res: Response) => {
      this.listData1 = res.json();
    });
  this.http.request('http://221.133.231.70:9000/nyse')
    .subscribe((res: Response) => {
      this.listData2 = res.json();
    });
  this.http.request('http://221.133.231.70:9000/market_heat')
    .subscribe((res: Response) => {
      this.listData3 = res.json();
    });
  this.http.request('http://221.133.231.70:9000/today_theme_z')
    .subscribe((res: Response) => {
      this.listData4 = res.json();
    });
  this.http.request('http://221.133.231.70:9000/today_theme_d')
    .subscribe((res: Response) => {
      this.listData5 = res.json();
    });
  
  }

  goTochart():void{
    this.navCtrl.push('realPage');
  }


}
