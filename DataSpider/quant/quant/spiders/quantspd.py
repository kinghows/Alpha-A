#!/usr/bin/env python
# -*- coding:utf-8 -*-
import scrapy
from scrapy import Selector
import MySQLdb
import urllib2
import json

import sys
reload(sys)
sys.setdefaultencoding('gbk')

import time
from datetime import datetime,date
date=time.strftime("%Y-%m-%d")
itime=int(time.strftime("%H%M"))
dayofweek = int(datetime.now().weekday())
print itime

class quantspd(scrapy.spiders.Spider):
    name = "quant"
    allowed_domains = ["xuangubao.cn"]
    start_urls = [
        "http://xuangubao.cn/",
    ]

    def parse(self, response):
        url1 = "http://xuangubao.cn/"
        yield scrapy.Request(url1, callback=self.parse1)

    def f_get_conn(self):
        try:
            conn = MySQLdb.connect(host='192.168.1.31', user='quant', passwd='quant', db='quant', port=3306)
	    cur = conn.cursor()
	    conn.set_character_set('utf8')
            cur.execute('SET NAMES utf8;') 
            cur.execute('SET CHARACTER SET utf8;')
	    cur.execute('SET character_set_connection=utf8;')
            return conn
        except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])
            sys.exit(1)
 
    def parse1(self, response):
	selector = Selector(response)
	conn = self.f_get_conn()
	cur = conn.cursor()
        rows=[]

	sql="SELECT MAX(createdatinsec) FROM hotspot "
	cur.execute(sql)
        ncreatedatinsec=cur.fetchone()[0]
	if ncreatedatinsec is None:
	    cur_time = time.time()  
	    ncreatedatinsec=str(cur_time-cur_time%86400) [0:10]

        html = urllib2.urlopen("https://api.xuangubao.cn/api/pc/msgs?headmark="+ncreatedatinsec+"&limit=30&subjids=9,10,723,35,469")
        jsonmsgs = json.loads(html.read())['NewMsgs']

        if jsonmsgs is not None:
            for msg in jsonmsgs:
	        createdatinsec=msg['CreatedAtInSec']
                timeStr=time.strftime("%Y-%m-%d %H:%M", time.localtime(createdatinsec))
                msgdate=timeStr[0:10]
		msgtime=timeStr[11:16]
    	        id=msg['Id']
	        title=msg['Title']
	        detail=msg['Summary'].replace('选股宝注：','').replace('选股宝讯，','')
	        stock_groups=[]
	        if msg['Stocks']:
	            for Stocks in msg['Stocks']:
	                stock_groups.append(Stocks['Name'])
		    stock_group = ",".join(stock_groups)
                else:
	            stock_group=''
	        themes=[]
	        if msg['BkjInfoArr']:
	            for BkjInfoArr in msg['BkjInfoArr']:
	                themes.append(BkjInfoArr['Name'])
		    theme = ",".join(themes)
                else:
	            if title.find("整点回顾") !=-1:
		        theme="整点回顾".decode('gbk').encode('utf8')      
		    elif (title.find("港股") !=-1) or (title.find("恒生") !=-1):
		        theme="港股".decode('gbk').encode('utf8')   
		    elif title.find("收评") !=-1:
		        theme="收评".decode('gbk').encode('utf8')   
		    elif title.find("大盘回顾") !=-1:
		        theme="收评".decode('gbk').encode('utf8')
		    elif title.find("期货") !=-1:
		        theme="期货".decode('gbk').encode('utf8')   
		    elif title.find("资金流向") !=-1:
		        theme="资金流向".decode('gbk').encode('utf8')   
		    elif title.find("复盘") !=-1:
		        theme="复盘".decode('gbk').encode('utf8')   
		    elif title.find("两市融资") !=-1:
		        theme="两市融资".decode('gbk').encode('utf8')   
		    elif title.find("两市") !=-1:
		        theme="开盘".decode('gbk').encode('utf8')   
		    elif title.find("新股开板") !=-1:
		        theme="新股开板".decode('gbk').encode('utf8')   
		    else:
	                theme=''
                
                rows.append((msgdate,msgtime,id,title,detail,theme,stock_group,createdatinsec))

	    sql = "insert into hotspot (date,time,id,title,detail,theme,stock_group,createdatinsec) values (%s,%s,%s,%s,%s,%s,%s,%s)"
	    cur.executemany(sql, rows)
            conn.commit()
	
        if itime >= 2340:
            sql = "INSERT INTO hotspot_his (theme,date,time,id,title,detail,stock_group,createdatinsec) SELECT theme,date,time,id,title,detail,stock_group,createdatinsec  FROM hotspot"
	    cur.execute(sql)
	    sql = "DELETE FROM hotspot"
	    cur.execute(sql)
            conn.commit()

        if (dayofweek in range(0, 5)) and ((itime in range(924, 1135)) or (itime in range(1304, 1505))) :
	    #股指
	    rows=[]
            html = urllib2.urlopen("https://api-ddc-wscn.xuangubao.cn/market/real?fields=prod_name,trade_status,update_time,last_px,px_change,px_change_rate,preclose_px,open_px,high_px,low_px,amplitude,turnover_ratio,pe_rate,dyn_pe,dyn_pb_rate,market_value,circulation_value,turnover_volume,turnover_value,hq_type_code,securities_type,volume_ratio,circulation_shares,total_shares,bps&prod_code=000001.SS")
            jsonindex = json.loads(html.read())['data']['snapshot']['000001.SS']
            index="上证指数".decode('gbk').encode('utf8') 
            code='sh'
	    ivalue = str(round(jsonindex[3],2))
	    ichange =  str(round(jsonindex[4],2))
	    iratio =  str(round(jsonindex[5],2))+'%'
	    rows.append((date,itime,index,ivalue,ichange,iratio,code))
            html = urllib2.urlopen("https://api-ddc-wscn.xuangubao.cn/market/real?fields=prod_name,trade_status,update_time,last_px,px_change,px_change_rate,preclose_px,open_px,high_px,low_px,amplitude,turnover_ratio,pe_rate,dyn_pe,dyn_pb_rate,market_value,circulation_value,turnover_volume,turnover_value,hq_type_code,securities_type,volume_ratio,circulation_shares,total_shares,bps&prod_code=399001.SZ")
            jsonindex = json.loads(html.read())['data']['snapshot']['399001.SZ']
            index="深证成指".decode('gbk').encode('utf8') 
            code='sz'
	    ivalue = str(round(jsonindex[3],2))
	    ichange =  str(round(jsonindex[4],2))
	    iratio =  str(round(jsonindex[5],2))+'%'
	    rows.append((date,itime,index,ivalue,ichange,iratio,code))
	    html = urllib2.urlopen("https://api-ddc-wscn.xuangubao.cn/market/real?fields=prod_name,trade_status,update_time,last_px,px_change,px_change_rate,preclose_px,open_px,high_px,low_px,amplitude,turnover_ratio,pe_rate,dyn_pe,dyn_pb_rate,market_value,circulation_value,turnover_volume,turnover_value,hq_type_code,securities_type,volume_ratio,circulation_shares,total_shares,bps&prod_code=399006.SZ")
            jsonindex = json.loads(html.read())['data']['snapshot']['399006.SZ']
            index="创业板指".decode('gbk').encode('utf8') 
            code='cy'
	    ivalue = str(round(jsonindex[3],2))
	    ichange =  str(round(jsonindex[4],2))
	    iratio =  str(round(jsonindex[5],2))+'%'
	    rows.append((date,itime,index,ivalue,ichange,iratio,code))

            if itime <=930:
	        sql = "DELETE FROM stockindex"
	        cur.execute(sql)
	    sql = "insert into stockindex (date,time,indexs,ivalue,ichange,iratio,codes) values (%s,%s,%s,%s,%s,%s,%s)"
	    cur.executemany(sql, rows)
	    if itime >= 1500:
	        sql = "INSERT INTO stockindex_his (DATE,indexs,ivalue,ichange,iratio,codes) SELECT DATE,indexs,ivalue,ichange,iratio,codes FROM stockindex WHERE DATE = CURDATE() AND TIME=(SELECT MAX(TIME) FROM stockindex WHERE DATE = CURDATE())"
	        cur.execute(sql)
            conn.commit()

	    #涨跌家数
	    rows=[]
	    html = urllib2.urlopen("https://flash-api.xuangubao.cn/api/market_indicator/latest")
            jsonlatest = json.loads(html.read())['data']
            rose =  jsonlatest["rise_count"]
            fell =  jsonlatest["fall_count"]
            flat =  jsonlatest["stay_count"]
            rows.append((date,itime,rose,fell,flat))

	    if itime <= 930:
	        sql = "DELETE FROM nyse"
	        cur.execute(sql)
	    sql = "insert into nyse (date,time,rose,fell,flat) values (%s,%s,%s,%s,%s)"
	    cur.executemany(sql, rows)
	    if itime >= 1500:
	        sql = "INSERT INTO nyse_his (DATE,rose,fell,flat) SELECT DATE,rose,fell,flat FROM nyse WHERE DATE = CURDATE() AND TIME=(SELECT MAX(TIME) FROM nyse WHERE DATE = CURDATE())"
	        cur.execute(sql)
            conn.commit()

	    #市场真实热度
	    rows=[]
            limit_up =  jsonlatest["limit_up_count"]
            limit_lose =  jsonlatest["limit_down_count"]
            lose_ratio = str(round(jsonlatest["limit_up_broken_ratio"]*100))+'%'
            heat_ratio = str(round(jsonlatest["market_temperature"]))+'%'
            rows.append((date,itime,limit_up,limit_lose,lose_ratio,heat_ratio))
            
	    if itime <= 930:
	        sql= "DELETE FROM market_heat"
	        cur.execute(sql)
	    sql = "insert into market_heat (date,time,limit_up,limit_lose,lose_ratio,heat_ratio) values (%s,%s,%s,%s,%s,%s)"
	    cur.executemany(sql, rows)
	    if itime >= 1500:
	        sql = "INSERT INTO market_heat_his (DATE,limit_up,limit_lose,lose_ratio,heat_ratio) SELECT DATE,limit_up,limit_lose,lose_ratio,heat_ratio FROM market_heat WHERE  TIME=(SELECT MAX(TIME) FROM market_heat)"
	        cur.execute(sql)
            conn.commit()

	    #今日风口
            rows=[]
            codes=[]
            themes={}
            html = urllib2.urlopen("https://baoer-api.xuangubao.cn/api/v2/tab/recommend?module=trending_plates")
            jsontheme = json.loads(html.read())['data']['items']
            for theme in jsontheme:
                for stock in theme['stocks']:
                    codes.append(stock['symbol'])
                    themes[stock['symbol']]=theme['plate_name']

            strcode = ",".join(codes)
            html = urllib2.urlopen("https://flash-api.xuangubao.cn/api/stock/data?symbols="+strcode+"&fields=symbol,stock_chi_name,change_percent,price,turnover_ratio,non_restricted_capital,total_capital,per,limit_up_days,last_limit_up,limit_status,nearly_new_acc_pcp&strict=true")
            jsonstock = json.loads(html.read())['data']
        
            for i in jsonstock:
                row = jsonstock[i]
                stock_name = row['stock_chi_name']
                price = row['price']
                change_rate = str(round(float(row['change_percent']),2))+'%'
                turnover_ratio = str(round(float(row['turnover_ratio']),2))+'%'
                circulation_value = str(round(float(row['non_restricted_capital'])/100000000,2))+'亿'.decode('gbk').encode('utf8') 
                total_value = str(round(float(row['total_capital'])/100000000,2))+'亿'.decode('gbk').encode('utf8') 
                pe = str(round(float(row['per'])))
                rows.append((themes[i],date,itime,stock_name,price,change_rate,turnover_ratio,circulation_value,total_value,pe))
			
            if itime <= 930:
                sql = "DELETE FROM hot_pool"
                cur.execute(sql)
            sql = "insert into hot_pool (theme,date,time,stock_name,price,change_rate,turnover_ratio,circulation_value,total_value,pe) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cur.executemany(sql, rows)

            if itime >= 1500:
                sql = "INSERT INTO hot_pool_his (theme,DATE,stock_name,price,change_rate,turnover_ratio,circulation_value,total_value,pe) SELECT theme,DATE,stock_name,price,change_rate,turnover_ratio,circulation_value,total_value,pe FROM theme_pool WHERE TIME=(SELECT MAX(TIME) FROM theme_pool )"
                cur.execute(sql)
                conn.commit()

	    #主题
	    rows=[]
	    themes = {}
	    codes = []
            html = urllib2.urlopen("https://flash-api.xuangubao.cn/api/stage2/plate/top_info?count=9&fields=all")
            jsondata = json.loads(html.read())['data']

	    jsontop = jsondata['top_plate_info']
	    for plate in jsontop:
	        title ="涨幅榜".decode('gbk').encode('utf8') 
                theme =plate["plate_name"]
	        rate = str(round(plate["core_avg_pcp"]*100))+'%'
		zd = '+'
	        rows.append((date,itime,title,theme,rate,zd))
                items = plate["led_rising_stocks"]["items"]
	        for item in items:
	            themes[item["symbol"]]=theme
	            codes.append(item["symbol"])

	    jsonbottom = jsondata['bottom_plate_info']
	    for plate in jsonbottom:
	        title ="跌幅榜".decode('gbk').encode('utf8') 
                theme =plate["plate_name"]
	        rate = str(round(plate["core_avg_pcp"]*100))+'%'
		zd = '-'
	        rows.append((date,itime,title,theme,rate,zd))
                items = plate["led_falling_stocks"]["items"]
	        for item in items:
	            themes[item["symbol"]]=theme
	            codes.append(item["symbol"])

	    if itime <= 930:
	        sql = "DELETE FROM theme"
	        cur.execute(sql)
	    sql = "insert into theme (date,time,title,theme,rate,zd) values (%s,%s,%s,%s,%s,%s)"
	    cur.executemany(sql, rows)
	    if itime >= 1500:
	        sql = "INSERT INTO theme_his (DATE,title,theme,rate,zd) SELECT DATE,title,theme,rate,zd FROM theme WHERE DATE = CURDATE() AND TIME=(SELECT MAX(TIME) FROM theme WHERE DATE = CURDATE())"
	        cur.execute(sql)
            conn.commit()

	    #主题池
	    rows=[]
	    strcode = ",".join(codes)
            html = urllib2.urlopen("https://flash-api.xuangubao.cn/api/stock/data?symbols="+strcode+"&fields=symbol,stock_chi_name,change_percent,price,turnover_ratio,non_restricted_capital,total_capital,per,limit_up_days,last_limit_up,limit_status,nearly_new_acc_pcp&strict=true")
            jsonstock = json.loads(html.read())['data']
        
            for i in jsonstock:
                row = jsonstock[i]
                stock_name = row['stock_chi_name']
                price = row['price']
                change_rate = str(round(float(row['change_percent']),2))+'%'
                turnover_ratio = str(round(float(row['turnover_ratio']),2))+'%'
                circulation_value = str(round(float(row['non_restricted_capital'])/100000000,2))+'亿'.decode('gbk').encode('utf8') 
                total_value = str(round(float(row['total_capital'])/100000000,2))+'亿'.decode('gbk').encode('utf8') 
                pe = str(round(float(row['per'])))
                rows.append((themes[i],date,itime,stock_name,price,change_rate,turnover_ratio,circulation_value,total_value,pe))

	    if itime <= 930:
	        sql = "DELETE FROM theme_pool"
	        cur.execute(sql)
	    sql = "insert into theme_pool (theme,date,time,stock_name,price,change_rate,turnover_ratio,circulation_value,total_value,pe) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
	    cur.executemany(sql, rows)
	    if itime >= 1500:
	        sql = "INSERT INTO theme_pool_his (theme,DATE,stock_name,price,change_rate,turnover_ratio,circulation_value,total_value,pe) SELECT theme,DATE,stock_name,price,change_rate,turnover_ratio,circulation_value,total_value,pe FROM theme_pool WHERE TIME=(SELECT MAX(TIME) FROM theme_pool )"
	        cur.execute(sql)
            conn.commit()

        #新股池
	    rows=[]
	    html = urllib2.urlopen("https://flash-api.xuangubao.cn/api/pool/detail?pool_name=new_stock")
            jsonstock = json.loads(html.read())['data']
	    for row in jsonstock:
	        stock_name =row["stock_chi_name"]
	        price = row["price"]
		change_rate =str(round(float(row["change_percent"]),2))+'%'
		turnover_ratio = str(round(float(row["turnover_ratio"]),2))+'%'
		circulation_value = str(round(float(row["non_restricted_capital"])/100000000,2))+'亿'.decode('gbk').encode('utf8') 
		total_value = str(round(float(row["total_capital"])/100000000,2))+'亿'.decode('gbk').encode('utf8') 
		if row["new_stock_break_limit_up"]==0:
                    first_open_time=''
		else:
                    first_open_time = time.strftime('%H:%M:%S',time.localtime(row["new_stock_break_limit_up"]))
		before_open_count = row["new_stock_limit_up_days"]
		accumulated_pcp = str(round(float(row["nearly_new_acc_pcp"]),2))+'%'
		time_on_market = time.strftime('%Y-%m-%d',time.localtime(row["listed_date"]))
	        rows.append((date,itime,stock_name,price,change_rate,turnover_ratio,circulation_value,total_value,first_open_time,before_open_count,accumulated_pcp,time_on_market))

	    if itime <= 930:
	        sql = "DELETE FROM new_pool"
	        cur.execute(sql)
	    sql = "insert into new_pool (date,time,stock_name,price,change_rate,turnover_ratio,circulation_value,total_value,first_open_time,before_open_count,accumulated_pcp,time_on_market) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
	    cur.executemany(sql, rows)
	    if itime >= 1500:
	        sql = "INSERT INTO new_pool_his (DATE,stock_name,price,change_rate,turnover_ratio,circulation_value,total_value,first_open_time,before_open_count,accumulated_pcp,time_on_market) SELECT DATE,stock_name,price,change_rate,turnover_ratio,circulation_value,total_value,first_open_time,before_open_count,accumulated_pcp,time_on_market FROM new_pool WHERE TIME=(SELECT MAX(TIME) FROM new_pool)"
	        cur.execute(sql)
            conn.commit()

            #次新池
	    rows=[]
	    html = urllib2.urlopen("https://flash-api.xuangubao.cn/api/pool/detail?pool_name=nearly_new")
            jsonstock = json.loads(html.read())['data']
	    for row in jsonstock:
	        stock_name =row["stock_chi_name"]
	        price = row["price"]
		change_rate =str(round(float(row["change_percent"]),2))+'%'
		turnover_ratio = str(round(float(row["turnover_ratio"]),2))+'%'
		circulation_value = str(round(float(row["non_restricted_capital"])/100000000,2))+'亿'.decode('gbk').encode('utf8') 
		total_value = str(round(float(row["total_capital"])/100000000,2))+'亿'.decode('gbk').encode('utf8') 
		open_board_day = row["nearly_new_break_days"]
		before_open_count = row["new_stock_limit_up_days"]
		accumulated_pcp = str(round(float(row["nearly_new_acc_pcp"]),2))+'%'
		time_on_market = time.strftime('%Y-%m-%d',time.localtime(row["listed_date"]))
	        rows.append((date,itime,stock_name,price,change_rate,turnover_ratio,circulation_value,total_value,open_board_day,before_open_count,accumulated_pcp,time_on_market))

	    if itime <= 930:
	        sql = "DELETE FROM cnew_pool"
	        cur.execute(sql)
	    sql = "insert into cnew_pool (date,time,stock_name,price,change_rate,turnover_ratio,circulation_value,total_value,open_board_day,before_open_count,accumulated_pcp,time_on_market) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
	    cur.executemany(sql, rows)
	    if itime >= 1500:
	        sql = "INSERT INTO cnew_pool_his (DATE,stock_name,price,change_rate,turnover_ratio,circulation_value,total_value,open_board_day,before_open_count,accumulated_pcp,time_on_market) SELECT DATE,stock_name,price,change_rate,turnover_ratio,circulation_value,total_value,open_board_day,before_open_count,accumulated_pcp,time_on_market FROM cnew_pool WHERE TIME=(SELECT MAX(TIME) FROM cnew_pool)"
	        cur.execute(sql)
            conn.commit()

            #强势池
	    rows=[]
	    html = urllib2.urlopen("https://flash-api.xuangubao.cn/api/pool/detail?pool_name=super_stock")
            jsonstock = json.loads(html.read())['data']
	    for row in jsonstock:
	        stock_name =row["stock_chi_name"]
		reason = row["surge_reason"]["stock_reason"]
	        price = row["price"]
		change_rate =str(round(float(row["change_percent"]),2))+'%'
		turnover_ratio = str(round(float(row["turnover_ratio"]),2))+'%'
		circulation_value = str(round(float(row["non_restricted_capital"])/100000000,2))+'亿'.decode('gbk').encode('utf8') 
		total_value = str(round(float(row["total_capital"])/100000000,2))+'亿'.decode('gbk').encode('utf8') 
		continue_board_count = row["limit_up_days"]
		board_days = str(row["m_days_n_boards_days"])+'天'.decode('gbk').encode('utf8')+str(row["m_days_n_boards_boards"])+'板'.decode('gbk').encode('utf8') 
	        rows.append((date,itime,stock_name,reason,price,change_rate,turnover_ratio,circulation_value,total_value,continue_board_count,board_days))

	    if itime <= 930:
	        sql = "DELETE FROM strong_pool"
	        cur.execute(sql)
	    sql = "insert into strong_pool (date,time,stock_name,reason,price,change_rate,turnover_ratio,circulation_value,total_value,continue_board_count,board_days) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
	    cur.executemany(sql, rows)
	    if itime >= 1500:
	        sql = "INSERT INTO strong_pool_his (DATE,stock_name,reason,price,change_rate,turnover_ratio,circulation_value,total_value,continue_board_count,board_days) SELECT DATE,stock_name,reason,price,change_rate,turnover_ratio,circulation_value,total_value,continue_board_count,board_days FROM strong_pool WHERE TIME=(SELECT MAX(TIME) FROM strong_pool)"
	        cur.execute(sql)
            conn.commit()

	    #涨停池
	    rows=[]
	    html = urllib2.urlopen("https://flash-api.xuangubao.cn/api/pool/detail?pool_name=limit_up")
            jsonstock = json.loads(html.read())['data']
	    for row in jsonstock:
	        stock_name =row["stock_chi_name"]
		reason =  row["surge_reason"]["stock_reason"]
	        price = row["price"]
		change_rate =str(round(float(row["change_percent"]),2))+'%'
		blockade_ratio = str(round(float(row["buy_lock_volume_ratio"]),2))+'%'
		turnover_ratio =str(round(float(row["turnover_ratio"]),2))+'%'
		circulation_value =str(round(float(row["non_restricted_capital"])/100000000,2))+'亿'.decode('gbk').encode('utf8') 
		total_value = str(round(float(row["total_capital"])/100000000,2))+'亿'.decode('gbk').encode('utf8') 
		first_raise_time = time.strftime('%H:%M:%S',time.localtime(row["first_limit_up"]))
		last_raise_time = time.strftime('%H:%M:%S',time.localtime(row["last_limit_up"]))
		open_count = row["break_limit_up_times"]
		continue_board_count = row["limit_up_days"]
	        rows.append((date,itime,stock_name,reason,price,change_rate,blockade_ratio,turnover_ratio,circulation_value,total_value,first_raise_time,last_raise_time,open_count,continue_board_count))

	    if itime <= 930:
	        sql = "DELETE FROM hit_pool"
	        cur.execute(sql)
	    sql = "insert into hit_pool (date,time,stock_name,reason,price,change_rate,blockade_ratio,turnover_ratio,circulation_value,total_value,first_raise_time,last_raise_time,open_count,continue_board_count) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
	    cur.executemany(sql, rows)
	    if itime >= 1500:
	        sql = "INSERT INTO hit_pool_his (DATE,stock_name,reason,price,change_rate,blockade_ratio,turnover_ratio,circulation_value,total_value,first_raise_time,last_raise_time,open_count,continue_board_count) SELECT DATE,stock_name,reason,price,change_rate,blockade_ratio,turnover_ratio,circulation_value,total_value,first_raise_time,last_raise_time,open_count,continue_board_count FROM hit_pool WHERE TIME=(SELECT MAX(TIME) FROM hit_pool)"
	        cur.execute(sql)
            conn.commit()


            #炸板池
	    rows=[]
	    html = urllib2.urlopen("https://flash-api.xuangubao.cn/api/pool/detail?pool_name=limit_up_broken")
            jsonstock = json.loads(html.read())['data']
	    for row in jsonstock:
	        stock_name =row["stock_chi_name"]
		reason =  row["surge_reason"]["stock_reason"]
	        price = row["price"]
		change_rate =str(round(float(row["change_percent"]),2))+'%'
		turnover_ratio =str(round(float(row["turnover_ratio"]),2))+'%'
		circulation_value =str(round(float(row["non_restricted_capital"])/100000000,2))+'亿'.decode('gbk').encode('utf8') 
		total_value = str(round(float(row["total_capital"])/100000000,2))+'亿'.decode('gbk').encode('utf8') 
		first_raise_time = time.strftime('%H:%M:%S',time.localtime(row["first_limit_up"]))
		last_raise_time = time.strftime('%H:%M:%S',time.localtime(row["last_limit_up"]))
		last_boom_time =  time.strftime('%H:%M:%S',time.localtime(row["last_break_limit_up"]))
		open_count = row["break_limit_up_times"]
		continue_board_count = row["limit_up_days"]
	        rows.append((date,itime,stock_name,reason,price,change_rate,turnover_ratio,circulation_value,total_value,first_raise_time,last_raise_time,last_boom_time,open_count,continue_board_count))

	    if itime <= 930:
	        sql = "DELETE FROM boom_pool"
	        cur.execute(sql)
	    sql = "insert into boom_pool (date,time,stock_name,reason,price,change_rate,turnover_ratio,circulation_value,total_value,first_raise_time,last_raise_time,last_boom_time,open_count,continue_board_count) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
	    cur.executemany(sql, rows)
	    if itime >= 1500:
	        sql = "INSERT INTO boom_pool_his (DATE,stock_name,reason,price,change_rate,turnover_ratio,circulation_value,total_value,first_raise_time,last_raise_time,last_boom_time,open_count,continue_board_count) SELECT DATE,stock_name,reason,price,change_rate,turnover_ratio,circulation_value,total_value,first_raise_time,last_raise_time,last_boom_time,open_count,continue_board_count FROM boom_pool WHERE TIME=(SELECT MAX(TIME) FROM boom_pool )"
	        cur.execute(sql)
            conn.commit()

	    #跌停池
	    rows=[]
	    html = urllib2.urlopen("https://flash-api.xuangubao.cn/api/pool/detail?pool_name=limit_down")
            jsonstock = json.loads(html.read())['data']
	    for row in jsonstock:
	        stock_name =row["stock_chi_name"]
	        price = row["price"]
		change_rate =str(round(float(row["change_percent"]),2))+'%'
		blockade_ratio = str(round(float(row["buy_lock_volume_ratio"]),2))+'%'
		turnover_ratio =str(round(float(row["turnover_ratio"]),2))+'%'
		circulation_value =str(round(float(row["non_restricted_capital"])/100000000,2))+'亿'.decode('gbk').encode('utf8') 
		total_value = str(round(float(row["total_capital"])/100000000,2))+'亿'.decode('gbk').encode('utf8') 
		first_board_time = time.strftime('%H:%M:%S',time.localtime(row["first_limit_up"]))
		last_board_time = time.strftime('%H:%M:%S',time.localtime(row["last_limit_up"]))
		open_count = row["break_limit_up_times"]
		continue_board_count = row["limit_up_days"]
	        rows.append((date,itime,stock_name,price,change_rate,blockade_ratio,turnover_ratio,circulation_value,total_value,first_board_time,last_board_time,open_count,continue_board_count))

	    if itime <= 930:
	        sql = "DELETE FROM down_pool"
	        cur.execute(sql)
	    sql = "insert into down_pool (date,time,stock_name,price,change_rate,blockade_ratio,turnover_ratio,circulation_value,total_value,first_board_time,last_board_time,open_count,continue_board_count) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
	    cur.executemany(sql, rows)
	    if itime >= 1500:
	        sql = "INSERT INTO down_pool_his (DATE,stock_name,price,change_rate,blockade_ratio,turnover_ratio,circulation_value,total_value,first_board_time,last_board_time,open_count,continue_board_count) SELECT DATE,stock_name,price,change_rate,blockade_ratio,turnover_ratio,circulation_value,total_value,first_board_time,last_board_time,open_count,continue_board_count FROM down_pool WHERE TIME=(SELECT MAX(TIME) FROM down_pool)"
	        cur.execute(sql)
            conn.commit()

	    #昨日涨停池
	    rows=[]
	    html = urllib2.urlopen("https://flash-api.xuangubao.cn/api/pool/detail?pool_name=yesterday_limit_up")
            jsonstock = json.loads(html.read())['data']
	    for row in jsonstock:
	        stock_name =row["stock_chi_name"]
		reason =  row["surge_reason"]["stock_reason"]
	        price = row["price"]
		change_rate =str(round(float(row["change_percent"]),2))+'%'
		turnover_ratio =str(round(float(row["turnover_ratio"]),2))+'%'
		circulation_value =str(round(float(row["non_restricted_capital"])/100000000,2))+'亿'.decode('gbk').encode('utf8') 
		total_value = str(round(float(row["total_capital"])/100000000,2))+'亿'.decode('gbk').encode('utf8') 
		first_raise_time = time.strftime('%H:%M:%S',time.localtime(row["first_limit_up"]))
		last_raise_time = time.strftime('%H:%M:%S',time.localtime(row["last_limit_up"]))
		open_count = row["break_limit_up_times"]
		continue_board_count = row["limit_up_days"]
	        rows.append((date,itime,stock_name,reason,price,change_rate,turnover_ratio,circulation_value,total_value,first_raise_time,last_raise_time,open_count,continue_board_count))

	    if itime <= 930:
	        sql = "DELETE FROM pre_hit_pool"
	        cur.execute(sql)
	    sql = "insert into pre_hit_pool (date,time,stock_name,reason,price,change_rate,turnover_ratio,circulation_value,total_value,first_raise_time,last_raise_time,open_count,continue_board_count) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
	    cur.executemany(sql, rows)
	    if itime >= 1500:
	        sql = "INSERT INTO pre_hit_pool_his (DATE,stock_name,reason,price,change_rate,turnover_ratio,circulation_value,total_value,first_raise_time,last_raise_time,open_count,continue_board_count) SELECT DATE,stock_name,reason,price,change_rate,turnover_ratio,circulation_value,total_value,first_raise_time,last_raise_time,open_count,continue_board_count FROM pre_hit_pool WHERE TIME=(SELECT MAX(TIME) FROM pre_hit_pool )"
	        cur.execute(sql)
            conn.commit()

	    #异动股票
	    rows=[]
	    html = urllib2.urlopen("https://flash-api.xuangubao.cn/api/pool/bubble")
            jsonstock = json.loads(html.read())['data']
	    for row in jsonstock:
	        stock_name =row["stock_chi_name"]
		last_px = row["price"]
	        pcp = row["new_stock_acc_pcp"]
		pcr = row["change_percent"]
		theme = ''
	        rows.append((date,itime,stock_name,last_px,pcp,pcr,theme))

	    if itime <= 930:
	        sql = "DELETE FROM fast_pool"
	        cur.execute(sql)
	    sql = "insert into fast_pool (date,time,stock_name,last_px,pcp,pcr,theme) values (%s,%s,%s,%s,%s,%s,%s)"
	    cur.executemany(sql, rows)
	    if itime >= 1500:
	        sql = "INSERT INTO fast_pool_his (DATE,time,stock_name,last_px,pcp,pcr,theme) SELECT DATE,time,stock_name,last_px,pcp,pcr,theme FROM fast_pool WHERE  last_px <>0 AND pcr>=3 ORDER BY stock_name,TIME"
	        cur.execute(sql)
            conn.commit()

    	cur.close()
    	conn.close()