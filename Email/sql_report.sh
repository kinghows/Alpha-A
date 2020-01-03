#!/bin/sh
report_base=/root/report
datetime=`date +%Y-%m-%d_%H-%M`
old_date1=`date +%Y-%m-%d_%H-%M -d -1days`
old_date3=`date +%Y-%m-%d_%H-%M -d -3days`
cd $report_base
/usr/local/bin/python $report_base/sql_report.py -p $report_base/dbset.ini  -s html>$report_base/A-share_$datetime.html
/usr/local/bin/python $report_base/SendEmail.py -p $report_base/emailset.ini -f $report_base/A-share_$datetime.html
rm -f A-share_$old_date1.html
rm -f A-share_$old_date3.html