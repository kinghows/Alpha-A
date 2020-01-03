#!/bin/sh
export PATH=$PATH:/usr/local/bin
cd /root/quant
nohup scrapy crawl quant  >> quant.log 2>&1 &