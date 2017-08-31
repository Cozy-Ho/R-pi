#!/bin/sh

/home/pi/cronf/check/system_check.sh > /home/pi/cronf/check/system_check.log 2>&1
/usr/sbin/ssmtp kj2693119@gmail.com < /home/pi/cronf/check/system_check.log 

