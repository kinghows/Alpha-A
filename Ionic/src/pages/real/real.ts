import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { Http, Response } from '@angular/http';

import * as ChartJs from 'chart.js'; // 导入chart.js

@IonicPage()
@Component({
  selector: 'page-real',
  templateUrl: 'real.html',
})
export class realPage {
  listData_sh: Object;
  listData_sz: Object;
  listData_cy: Object;

  constructor(public navCtrl: NavController, public navParams: NavParams,private http: Http) {
  }

  ionViewDidLoad() {
    this.http.request('http://221.133.231.70:9000/chart_sh')
    .subscribe((res: Response) => {
      this.listData_sh = res.json();
    });
    this.http.request('http://221.133.231.70:9000/chart_sz')
    .subscribe((res: Response) => {
      this.listData_sz = res.json();
    });
    this.http.request('http://221.133.231.70:9000/chart_cy')
    .subscribe((res: Response) => {
      this.listData_cy = res.json();
    });
  }

  ionViewDidEnter() {
    var canvas_sh = <HTMLCanvasElement> document.getElementById('myChart_sh');
    var ctx_sh = canvas_sh.getContext('2d');
    ChartJs.Line(ctx_sh,{
      data: {
        labels: [930, 935, 940, 945, 950, 955, 1000, 1005, 1010, 1015, 1020, 1025, 1030, 1035, 1040, 1045, 1050, 1055, 1100, 1105, 1110, 1115, 1120, 1125, 1130,1305,1310,1315,1320, 1325, 1330, 1335,1340, 1345, 1350, 1355, 1400, 1405, 1410, 1415, 1420, 1425, 1430, 1435, 1440, 1445, 1450, 1455, 1500],
        datasets: [{
          label: '上证指数',
          data: this.listData_sh ,
          backgroundColor: [
            'rgba(255, 99, 132, 0.2)'
          ],
          borderColor: [
            'rgba(255,99,132,1)'
          ],
          //点外圈颜色
          pointBorderColor : "rgba(220, 220, 220, 0.5)", 
          //点的颜色
          pointBackgroundColor : "rgba(220, 220, 220, 0.5)", 
          //点外圈宽度
          pointBorderWidth : 0, 
          //点半径
          pointRadius : 0, 
          // TODO 
          pointHitRadius : 0, 
          //鼠标悬浮时点半径    
          pointHoverRadius : 0, 
          //鼠标悬浮时点的颜色   
          pointHoverBackgroundColor : "rgba(220, 220, 220, 0.5)", 
          //鼠标悬浮时点边框颜色
          pointHoverBorderColor : "rgba(220, 220, 220, 0.5)", 
          //鼠标悬浮时点半径 
          pointHoverBorderWidth : 0, 
          //点的样式  
          pointStyle : "triangle", 
          //是否绘制线条  
          showLine : true, 
          //有空数据时是否绘制 
          spanGaps : false, 
          //是否为阶梯图
          steppedLine : false,
          //是否填充(线条下方区域填充)
          fill : true,
          borderWidth: 1
        }]
      },
    
      options: {scales: {yAxes: [{ticks: {beginAtZero:false}}]},
                legend: {labels : {
                                   //图例框宽度
                                   boxWidth : 0,
                                   //图例字体样式
                                   fontSize : 12,
                                   fontStyle : "normal",
                                   fontColor : "#666",
                                   fontFamily : "'Helvetica Neue', 'Helvetica', 'Arial', sans-serif",
                                   //图例上下边距
                                   padding : 10,}}
                }

    })
    
    var canvas_sz = <HTMLCanvasElement> document.getElementById('myChart_sz');
    var ctx_sz = canvas_sz.getContext('2d');
    ChartJs.Line(ctx_sz,{
      data: {
        labels: [930, 935, 940, 945, 950, 955, 1000, 1005, 1010, 1015, 1020, 1025, 1030, 1035, 1040, 1045, 1050, 1055, 1100, 1105, 1110, 1115, 1120, 1125, 1130,1305,1310,1315,1320, 1325, 1330, 1335,1340, 1345, 1350, 1355, 1400, 1405, 1410, 1415, 1420, 1425, 1430, 1435, 1440, 1445, 1450, 1455, 1500],
        datasets: [{
          label: '深证指数',
          data: this.listData_sz,
          backgroundColor: [
            'rgba(255, 99, 132, 0.2)'
          ],
          borderColor: [
            'rgba(255,99,132,1)'
          ],
          //点外圈颜色
          pointBorderColor : "rgba(220, 220, 220, 0.5)", 
          //点的颜色
          pointBackgroundColor : "rgba(220, 220, 220, 0.5)", 
          //点外圈宽度
          pointBorderWidth : 0, 
          //点半径
          pointRadius : 0, 
          // TODO 
          pointHitRadius : 0, 
          //鼠标悬浮时点半径    
          pointHoverRadius : 0, 
          //鼠标悬浮时点的颜色   
          pointHoverBackgroundColor : "rgba(220, 220, 220, 0.5)", 
          //鼠标悬浮时点边框颜色
          pointHoverBorderColor : "rgba(220, 220, 220, 0.5)", 
          //鼠标悬浮时点半径 
          pointHoverBorderWidth : 0, 
          //点的样式  
          pointStyle : "triangle", 
          //是否绘制线条  
          showLine : true, 
          //有空数据时是否绘制 
          spanGaps : false, 
          //是否为阶梯图
          steppedLine : false,
          //是否填充(线条下方区域填充)
          fill : true,
          borderWidth: 1
        }]
      },
    
      options: {scales: {yAxes: [{ticks: {beginAtZero:false}}]},
                legend: {labels : {
                                   //图例框宽度
                                   boxWidth : 0,
                                   //图例字体样式
                                   fontSize : 12,
                                   fontStyle : "normal",
                                   fontColor : "#666",
                                   fontFamily : "'Helvetica Neue', 'Helvetica', 'Arial', sans-serif",
                                   //图例上下边距
                                   padding : 10,}}
                }

      })

    var canvas_cy = <HTMLCanvasElement> document.getElementById('myChart_cy');
    var ctx_cy = canvas_cy.getContext('2d');
    ChartJs.Line(ctx_cy,{
      data: {
        labels: [930, 935, 940, 945, 950, 955, 1000, 1005, 1010, 1015, 1020, 1025, 1030, 1035, 1040, 1045, 1050, 1055, 1100, 1105, 1110, 1115, 1120, 1125, 1130,1305,1310,1315,1320, 1325, 1330, 1335,1340, 1345, 1350, 1355, 1400, 1405, 1410, 1415, 1420, 1425, 1430, 1435, 1440, 1445, 1450, 1455, 1500],
        datasets: [{
          label: '创业板指',
          data: this.listData_cy,
          backgroundColor: [
            'rgba(255, 99, 132, 0.2)'
          ],
          borderColor: [
            'rgba(255,99,132,1)'
          ],
          //点外圈颜色
          pointBorderColor : "rgba(220, 220, 220, 0.5)", 
          //点的颜色
          pointBackgroundColor : "rgba(220, 220, 220, 0.5)", 
          //点外圈宽度
          pointBorderWidth : 0, 
          //点半径
          pointRadius : 0, 
          // TODO 
          pointHitRadius : 0, 
          //鼠标悬浮时点半径    
          pointHoverRadius : 0, 
          //鼠标悬浮时点的颜色   
          pointHoverBackgroundColor : "rgba(220, 220, 220, 0.5)", 
          //鼠标悬浮时点边框颜色
          pointHoverBorderColor : "rgba(220, 220, 220, 0.5)", 
          //鼠标悬浮时点半径 
          pointHoverBorderWidth : 0, 
          //点的样式  
          pointStyle : "triangle", 
          //是否绘制线条  
          showLine : true, 
          //有空数据时是否绘制 
          spanGaps : false, 
          //是否为阶梯图
          steppedLine : false,
          //是否填充(线条下方区域填充)
          fill : true,
          borderWidth: 1
        }]
      },
    
      options: {scales: {yAxes: [{ticks: {beginAtZero:false}}]},
                legend: {labels : {
                                   //图例框宽度
                                   boxWidth : 0,
                                   //图例字体样式
                                   fontSize : 12,
                                   fontStyle : "normal",
                                   fontColor : "#666",
                                   fontFamily : "'Helvetica Neue', 'Helvetica', 'Arial', sans-serif",
                                   //图例上下边距
                                   padding : 10,}}
                }

      })
  }

}