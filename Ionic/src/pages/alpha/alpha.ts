import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';
import { Http, Response } from '@angular/http';

@Component({
  selector: 'page-alpha',
  templateUrl: 'alpha.html'
})
export class alphaPage {
  listData: Object;

  constructor(public navCtrl: NavController, private http: Http) {

  }

  ionViewDidLoad() {
    this.http.request('http://221.133.231.70:9000/alphaa')
    .subscribe((res: Response) => {
      this.listData = res.json();
    });
  }
}
