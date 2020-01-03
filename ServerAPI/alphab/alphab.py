# coding: utf-8
import falcon
import MySQLdb 
import json

def get_json(menu_item):
    try:
        if menu_item == 'stockindex' :
            query="""SELECT indexs,ivalue,ichange,iratio,LEFT(ichange,1) zd FROM stockindex WHERE TIME=(SELECT MAX(TIME) FROM stockindex WHERE DATE = CURDATE()) """
        elif menu_item =='nyse' :
            query="""SELECT rose,fell,flat FROM quant.nyse WHERE TIME=(SELECT MAX(TIME) FROM quant.nyse WHERE DATE = CURDATE())"""
        elif menu_item =='market_heat' :
            query="""SELECT heat_ratio,LEFT(heat_ratio,LENGTH(heat_ratio)-1) heat_ratio_n,limit_up,limit_lose,lose_ratio FROM quant.market_heat WHERE TIME=(SELECT MAX(TIME) FROM quant.market_heat WHERE DATE = CURDATE())"""
        elif menu_item =='today_theme_z' :
            query="""SELECT title,theme,rate FROM theme WHERE zd = "+" AND TIME=(SELECT MAX(TIME) FROM theme )"""
        elif menu_item =='today_theme_d' :
            query="""SELECT title,theme,rate FROM theme WHERE zd = "-" AND TIME=(SELECT MAX(TIME) FROM theme)"""
	elif menu_item =='today_stock' :
            query="""SELECT time,theme,stock_group,title,SUBSTR(detail,1,200) detail FROM quant.hotspot ORDER BY id DESC"""
        elif menu_item =='hot_pool' :
            query="""SELECT theme,stock_name,price,change_rate,turnover_ratio
                      FROM hot_pool WHERE  TIME=(SELECT MAX(TIME) FROM hot_pool)"""
        elif menu_item =='theme_pool' :
            query="""SELECT theme,stock_name,price,change_rate,turnover_ratio
                      FROM theme_pool WHERE TIME=(SELECT MAX(TIME) FROM theme_pool )"""
        elif menu_item =='strong_pool' :
            query="""SELECT stock_name,price,change_rate,turnover_ratio,board_days
                          FROM strong_pool WHERE  TIME=(SELECT MAX(TIME) FROM strong_pool ) """
	elif menu_item =='hit_pool' :
            query="""SELECT stock_name,price,turnover_ratio,last_raise_time,blockade_ratio
                      FROM hit_pool WHERE  TIME=(SELECT MAX(TIME) FROM hit_pool )"""
        elif menu_item =='boom_pool' :
            query="""SELECT stock_name,price,change_rate,turnover_ratio,last_boom_time
                      FROM boom_pool WHERE  TIME=(SELECT MAX(TIME) FROM boom_pool)"""
        elif menu_item =='new_pool' :
            query="""SELECT stock_name,price,change_rate,turnover_ratio,before_open_count
                          FROM new_pool WHERE  TIME=(SELECT MAX(TIME) FROM new_pool )"""
        elif menu_item =='cnew_pool' :
            query="""SELECT stock_name,price,change_rate,turnover_ratio,open_board_day
                          FROM cnew_pool WHERE TIME=(SELECT MAX(TIME) FROM cnew_pool)"""
	elif menu_item =='down_pool' :
            query="""SELECT a.stock_name,price,turnover_ratio,last_board_time,blockade_ratio FROM down_pool a
                          ,(SELECT stock_name,MAX(TIME) AS tt FROM down_pool GROUP BY stock_name ) b 
                            WHERE a.stock_name =b.stock_name AND a.time = b.tt ORDER BY last_board_time DESC"""
	elif menu_item =='pre_hit_pool' :
            query="""SELECT stock_name,price,change_rate,turnover_ratio,last_raise_time
                      FROM pre_hit_pool WHERE  TIME=(SELECT MAX(TIME) FROM pre_hit_pool) ORDER BY change_rate DESC"""
	elif menu_item =='fast_pool' :
            query="""SELECT stock_name,time,last_px,CONCAT(pcp,'%') pcp,pcr,theme 
	              FROM fast_pool WHERE last_px <>0 AND (pcr>=2 OR pcr<=-2) ORDER BY TIME DESC"""
        elif menu_item =='alphaa' :
            query="""SELECT date,time,title,detail FROM alphaa ORDER BY tid DESC LIMIT 10"""

        conn = MySQLdb.connect(host='127.0.0.1', user='quant', passwd='quant', db='quant', port=3306)
        cursor = conn.cursor()
        cursor.execute('SET NAMES UTF8')
        cursor.execute(query)
        rows = cursor.fetchall()
	fields = cursor.description
        
        column_list = [] 
	for i in fields:
	    column_list.append(i[0])

        datajson = []
        for row in rows:
            result = {}
            n = 0
	    for col in row:
                result[column_list[n]] = str(col)
		n += 1
            datajson.append(result)

	jsondata=json.dumps(datajson,ensure_ascii=False)
	return jsondata

    except Exception, Argment:
        return Argment

def get_json2(menu_item):
    try:
        if menu_item == 'chart_sh' :
            query="""SELECT ivalue FROM stockindex where codes='sh'"""
        elif menu_item =='chart_sz' :
            query="""SELECT ivalue FROM stockindex where codes='sz'"""
        elif menu_item =='chart_cy' :
            query="""SELECT ivalue FROM stockindex where codes='cy'"""

        conn = MySQLdb.connect(host='127.0.0.1', user='quant', passwd='quant', db='quant', port=3306)
        cursor = conn.cursor()
        cursor.execute('SET NAMES UTF8')
	cursor.execute(query)
        rows = cursor.fetchall()
        
        datajson = []
        for row in rows:
            datajson.append(row[0])

	jsondata=json.dumps(datajson,ensure_ascii=False)
	return jsondata

    except Exception, Argment:
        return Argment

class stockindex(object):
    def on_get(self, req, resp):
	resp.body = get_json('stockindex')
        resp.status = falcon.HTTP_200

class nyse(object):
    def on_get(self, req, resp):
	resp.body = get_json('nyse')
        resp.status = falcon.HTTP_200

class market_heat(object):
    def on_get(self, req, resp):
	resp.body = get_json('market_heat')
        resp.status = falcon.HTTP_200

class today_theme_z(object):
    def on_get(self, req, resp):
	resp.body = get_json('today_theme_z')
        resp.status = falcon.HTTP_200

class today_theme_d(object):
    def on_get(self, req, resp):
	resp.body = get_json('today_theme_d')
        resp.status = falcon.HTTP_200

class today_stock(object):
    def on_get(self, req, resp):
        resp.body = get_json('today_stock')
        resp.status = falcon.HTTP_200

class hot_pool(object):
    def on_get(self, req, resp):
	resp.body = get_json('hot_pool')
        resp.status = falcon.HTTP_200

class theme_pool(object):
    def on_get(self, req, resp):
	resp.body = get_json('theme_pool')
        resp.status = falcon.HTTP_200

class strong_pool(object):
    def on_get(self, req, resp):
	resp.body = get_json('strong_pool')
        resp.status = falcon.HTTP_200

class hit_pool(object):
    def on_get(self, req, resp):
	resp.body = get_json('hit_pool')
        resp.status = falcon.HTTP_200

class boom_pool(object):
    def on_get(self, req, resp):
	resp.body = get_json('boom_pool')
        resp.status = falcon.HTTP_200

class new_pool(object):
    def on_get(self, req, resp):
	resp.body = get_json('new_pool')
        resp.status = falcon.HTTP_200

class cnew_pool(object):
    def on_get(self, req, resp):
	resp.body = get_json('cnew_pool')
        resp.status = falcon.HTTP_200

class down_pool(object):
    def on_get(self, req, resp):
	resp.body = get_json('down_pool')
        resp.status = falcon.HTTP_200

class pre_hit_pool(object):
    def on_get(self, req, resp):
	resp.body = get_json('pre_hit_pool')
        resp.status = falcon.HTTP_200

class fast_pool(object):
    def on_get(self, req, resp):
	resp.body = get_json('fast_pool')
        resp.status = falcon.HTTP_200

class alphaa(object):
    def on_get(self, req, resp):
	resp.body = get_json('alphaa')
        resp.status = falcon.HTTP_200

class chart_sh(object):
    def on_get(self, req, resp):
	resp.body = get_json2('chart_sh')
        resp.status = falcon.HTTP_200

class chart_sz(object):
    def on_get(self, req, resp):
	resp.body = get_json2('chart_sz')
        resp.status = falcon.HTTP_200

class chart_cy(object):
    def on_get(self, req, resp):
	resp.body = get_json2('chart_cy')
        resp.status = falcon.HTTP_200
