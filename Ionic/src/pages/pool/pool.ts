import { Component, ViewChild } from '@angular/core';
import { NavController, NavParams,Platform,Slides } from 'ionic-angular';
import { Http, Response } from '@angular/http';

@Component({
  selector: 'page-pool',
  templateUrl: 'pool.html'
})
export class poolPage {
  listData0: Object;
  listData1: Object;
  listData2: Object;
  listData3: Object;
  listData4: Object;
  listData5: Object;
  listData6: Object;
  listData7: Object;
  listData8: Object;
  listData9: Object;
  @ViewChild('mySlider') slider: Slides;

  private selected_segment = 0;
  top_segment = 'top_0';
  segment = 'sites';

  rootNavCtrl: NavController;

  constructor(public navCtrl: NavController, public navParams: NavParams, public platform: Platform, private http: Http) {
    this.rootNavCtrl = navParams.get('rootNavCtrl');
    this.platform = platform;
  }

  ionViewDidLoad() {
    this.http.request('http://221.133.231.70:9000/fast_pool')
    .subscribe((res: Response) => {
      this.listData0 = res.json();
    });
    this.http.request('http://221.133.231.70:9000/hot_pool')
    .subscribe((res: Response) => {
      this.listData1 = res.json();
    });
    this.http.request('http://221.133.231.70:9000/theme_pool')
    .subscribe((res: Response) => {
      this.listData2 = res.json();
    });
    this.http.request('http://221.133.231.70:9000/strong_pool')
    .subscribe((res: Response) => {
      this.listData3 = res.json();
    });
    this.http.request('http://221.133.231.70:9000/hit_pool')
    .subscribe((res: Response) => {
      this.listData4 = res.json();
    });
    this.http.request('http://221.133.231.70:9000/pre_hit_pool')
    .subscribe((res: Response) => {
      this.listData5 = res.json();
    });
    this.http.request('http://221.133.231.70:9000/boom_pool')
    .subscribe((res: Response) => {
      this.listData6 = res.json();
    });
    this.http.request('http://221.133.231.70:9000/down_pool')
    .subscribe((res: Response) => {
      this.listData7 = res.json();
    });
    this.http.request('http://221.133.231.70:9000/new_pool')
    .subscribe((res: Response) => {
      this.listData8 = res.json();
    });
    this.http.request('http://221.133.231.70:9000/cnew_pool')
    .subscribe((res: Response) => {
      this.listData9 = res.json();
    });
  }
  
  select(index) 
  {
	if (index === 9){
		this.top_segment = 'top_9';
	}
	if (index === 8){
		this.top_segment = 'top_8';
	}
	if (index === 7){
		this.top_segment = 'top_7';
	}
    if (index === 6){
		this.top_segment = 'top_6';
	}
	if (index === 5){
		this.top_segment = 'top_5';
	}
	if (index === 4){
		this.top_segment = 'top_4';
	}
	if (index === 3){
		this.top_segment = 'top_3';
	}
	if (index === 2){
		this.top_segment = 'top_2';
	}
	if (index === 1){
		this.top_segment = 'top_1';
	}
	if (index === 0){
		this.top_segment = 'top_0';
	}
	this.slider.slideTo(index, 500);
  }

  select_segment(index) 
  {
	this.selected_segment = index;
	console.log("this.selected_segment: " + this.selected_segment);
  }

  onSlideChanged($event) 
  {
	if (((($event.touches.startX - $event.touches.currentX) <= 100) || (($event.touches.startX - $event.touches.currentX) > 0)) && (this.slider.isBeginning() || this.slider.isEnd())) 
	{
	  //console.log("interdit Direction");
	}
	else 
	{
	  //console.log("OK Direction");
	}

  }

  panEvent(e) 
  {
	let currentIndex = this.slider.getActiveIndex();
	if (currentIndex === 9){
	  this.top_segment = 'top_9';
	}
	if (currentIndex === 8){
	  this.top_segment = 'top_8';
	}
	if (currentIndex === 7){
	  this.top_segment = 'top_7';
	}
    if (currentIndex === 6){
	  this.top_segment = 'top_6';
	}
	if (currentIndex === 5){
	  this.top_segment = 'top_5';
	}
	if (currentIndex === 4){
	  this.top_segment = 'top_4';
	}
	if (currentIndex === 3){
	  this.top_segment = 'top_3';
	}
	if (currentIndex === 2){
	  this.top_segment = 'top_2';
	}
	if (currentIndex === 1){
	  this.top_segment = 'top_1';
	}
	if (currentIndex === 0){
	  this.top_segment = 'top_0';
	}
  }

}
