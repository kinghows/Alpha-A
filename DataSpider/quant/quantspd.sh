#!/bin/sh
export PATH=$PATH:/usr/local/bin
cd /root/quant
nohup /usr/local/bin/scrapy crawl quant  >> quant.log 2>&1 &