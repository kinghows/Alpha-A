# coding: utf-8
# filename: handle.py

import hashlib
import reply
import receive
import web
import MySQLdb
import sys

class Handle(object):
    def GET(self):
        try:
            data = web.input()
            if len(data) == 0:
                return "Are you OK!"
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            token = "alpha2017" #请按照公众平台官网\基本配置中信息填写

            list = [token, timestamp, nonce]
            list.sort()
            sha1 = hashlib.sha1()
            map(sha1.update, list)
            hashcode = sha1.hexdigest()
            print "handle/GET func: hashcode, signature: ", hashcode, signature
            if hashcode == signature:
                return echostr
            else:
                return ""
        except Exception, Argument:
            return Argument

    def POST(self):
        try:
            webData = web.data()
            #print "Handle Post webdata is ", webData   #后台打日志
            recMsg = receive.parse_xml(webData)
            if isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'text':
                if recMsg.Content =='今日股市' :
                    query="""SELECT CONCAT_WS(' ',TIME,title,theme,stock_group) FROM hotspot WHERE  theme NOT IN ('收评','整点回顾','开盘','复盘','资金流向','') ORDER BY id DESC LIMIT 15"""
                elif recMsg.Content =='今日消息' :
                    query="""SELECT CONCAT_WS(' ',TIME,title,theme,stock_group) FROM hotspot WHERE  theme = '' ORDER BY id DESC LIMIT 20"""
                elif recMsg.Content =='今日主题' :
                    query="""SELECT CONCAT_WS(' ',title,theme,rate) FROM theme WHERE  TIME=(SELECT MAX(TIME) FROM theme )"""
                elif recMsg.Content =='今日风口' :
                    query="""SELECT '主题          ,股票名称,最新价,涨跌幅,换手率,    流通市值,  总市值,  市盈率' UNION ALL
                              SELECT CONCAT_WS(' ',RPAD(theme,12,' '),RPAD(stock_name,4,' '),LPAD(price,6,' '),LPAD(change_rate,6,' '),
                              LPAD(turnover_ratio,6,' '),LPAD(circulation_value,8,' '),LPAD(total_value,8,' '),LPAD(pe,8,' '))
                              FROM hot_pool WHERE  TIME=(SELECT MAX(TIME) FROM hot_pool ) LIMIT 20"""
                elif recMsg.Content =='主题池' :
                    query="""SELECT '主题          ,股票名称,最新价,涨跌幅,换手率,    流通市值,  总市值,  市盈率' UNION ALL
                              SELECT CONCAT_WS(' ',RPAD(theme,12,' '),RPAD(stock_name,4,' '),LPAD(price,6,' '),LPAD(change_rate,6,' '),
                              LPAD(turnover_ratio,6,' '),LPAD(circulation_value,8,' '),LPAD(total_value,8,' '),LPAD(pe,8,' '))
                              FROM theme_pool WHERE  TIME=(SELECT MAX(TIME) FROM theme_pool ) LIMIT 20"""
                elif recMsg.Content =='涨停池' :
                    query="""SELECT '股票名称,最新价,涨跌幅,封单比,换手率,流通市值,  总市值,首次封板,最后封板,开板数,连板数' UNION ALL
                              SELECT CONCAT_WS(' ',RPAD(stock_name,4,' '),LPAD(price,6,' '),LPAD(change_rate,6,' '),LPAD(blockade_ratio,6,' '),
                              LPAD(turnover_ratio,6,' '),LPAD(circulation_value,8,' '),LPAD(total_value,6,' '),first_raise_time,last_raise_time,
                              LPAD(open_count,5,' '),LPAD(continue_board_count,7,' '))
                              FROM hit_pool WHERE  TIME=(SELECT MAX(TIME) FROM hit_pool ) LIMIT 20"""
                elif recMsg.Content =='炸板池' :
                    query="""SELECT '股票名称,最新价,涨跌幅,换手率,流通市值,  总市值,首次封板,最后封板,最后炸板,开板次数,连板数' UNION ALL
                              SELECT CONCAT_WS(' ',RPAD(stock_name,4,' '),LPAD(price,6,' '),LPAD(change_rate,6,' '),
                              LPAD(turnover_ratio,6,' '),LPAD(circulation_value,8,' '),LPAD(total_value,6,' '),first_raise_time,last_raise_time,
                              last_boom_time,LPAD(open_count,5,' '),LPAD(continue_board_count,7,' '))
                              FROM boom_pool WHERE  TIME=(SELECT MAX(TIME) FROM boom_pool ) LIMIT 20"""
                elif recMsg.Content =='新股池' :
                    query="""SELECT '股票名称,最新价,涨跌幅,换手率,流通市值,  总市值,首次开板,前连板数,累计涨幅,上市日期' UNION ALL
                              SELECT CONCAT_WS(' ',RPAD(stock_name,4,' '),LPAD(price,6,' '),LPAD(change_rate,6,' '),
                              LPAD(turnover_ratio,6,' '),LPAD(circulation_value,7,' '),LPAD(total_value,7,' '),first_open_time,LPAD(before_open_count,5,' '),
                              LPAD(accumulated_pcp,10,' '),time_on_market)
                              FROM new_pool WHERE  TIME=(SELECT MAX(TIME) FROM new_pool ) LIMIT 20"""
                elif recMsg.Content =='次新池' :
                    query="""SELECT '股票名称,最新价,涨跌幅,换手率,流通市值,  总市值,开板天数,前连板数,开后累计涨幅,上市日期' UNION ALL
                              SELECT CONCAT_WS(' ',RPAD(stock_name,4,' '),LPAD(price,6,' '),LPAD(change_rate,6,' '),
                              LPAD(turnover_ratio,6,' '),LPAD(circulation_value,7,' '),LPAD(total_value,7,' '),LPAD(open_board_day,7,' '),
                              LPAD(before_open_count,9,' '),LPAD(accumulated_pcp,12,' '),time_on_market)
                              FROM cnew_pool WHERE  TIME=(SELECT MAX(TIME) FROM cnew_pool ) LIMIT 20"""
                elif recMsg.Content =='强势池' :
                    query="""SELECT '股票名称,最新价,涨跌幅,换手率,流通市值,  总市值,连板数,几天几板' UNION ALL
                              SELECT CONCAT_WS(' ',RPAD(stock_name,4,' '),LPAD(price,6,' '),LPAD(change_rate,6,' '),
                              LPAD(turnover_ratio,6,' '),LPAD(circulation_value,7,' '),LPAD(total_value,7,' '),LPAD(continue_board_count,5,' '),
                              LPAD(board_days,7,' '))
                              FROM strong_pool WHERE  TIME=(SELECT MAX(TIME) FROM strong_pool ) LIMIT 20"""
                elif recMsg.Content =='昨日主题' :
                    query="""SELECT CONCAT_WS(' ',title,theme,rate) FROM theme_his WHERE DATE = DATE_SUB(CURDATE(),INTERVAL 1 DAY)"""
                elif recMsg.Content == '收评' or recMsg.Content == '整点回顾' or recMsg.Content == '复盘'  or recMsg.Content == '开盘':
                    query="""SELECT CONCAT_WS(' ',TIME,title,detail) FROM hotspot WHERE  theme = '"""+recMsg.Content+"""'"""
                elif recMsg.Content == '资金流向' :
                    query="""SELECT CONCAT_WS(' ',title,detail) FROM hotspot WHERE theme = '资金流向' ORDER BY DATE DESC LIMIT 5"""
                elif recMsg.Content == '股指' :
                    query="""SELECT CONCAT_WS(' ',indexs,ivalue,ichange,iratio) FROM stockindex WHERE  TIME=(SELECT MAX(TIME) FROM stockindex ) UNION ALL
                              SELECT CONCAT_WS(' ','涨',rose,'跌',fell,'平',flat) FROM nyse WHERE  TIME=(SELECT MAX(TIME) FROM nyse ) UNION ALL
                              SELECT CONCAT_WS(' ','市场热度',heat_ratio,'涨停',limit_up,'炸板',limit_lose,'炸板率',lose_ratio) FROM market_heat WHERE  TIME=(SELECT MAX(TIME) FROM market_heat )"""
                elif recMsg.Content[0:9] =='涨跌榜' :
                    query="""SELECT CONCAT_WS(' ',DATE,theme,rate) FROM theme_his WHERE theme LIKE '%"""+recMsg.Content[10:]+"""%' ORDER BY DATE DESC  LIMIT 50"""
                elif recMsg.Content[0:6] =='龙头' :
                    query="""SELECT CONCAT_WS(' ',DATE,stock_name,change_rate) FROM theme_pool_his WHERE theme LIKE '%"""+recMsg.Content[7:]+"""%' ORDER BY DATE DESC  LIMIT 50"""
                else:
                    query = """SELECT CONCAT_WS(' ',DATE,title,stock_group) FROM hotspot WHERE theme LIKE '%"""+recMsg.Content+"""%' ORDER BY DATE DESC  LIMIT 15"""

                conn = MySQLdb.connect(host='127.0.0.1', user='quant', passwd='quant', db='quant', port=3306)
                cursor = conn.cursor()
                cursor.execute('SET NAMES UTF8')
                getNum = cursor.execute(query)
                content =recMsg.Content
                if getNum > 0:
                    records = cursor.fetchall()
                    for record in records:
                        content=content +'\n'+ str(record[0])
                else:
                    content = getNum

                cursor.close()
                conn.close()
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                replyMsg = reply.TextMsg(toUser, fromUser, content)
                return replyMsg.send()
            else:
                return "success"
        except Exception, Argment:
            return Argment