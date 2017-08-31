#!/bin/sh
echo "SUBJECT:System_Check_Mail"
echo  "==========================================="
hostname
echo  "==========================================="
echo  "\n ${bold} 0. TEMPERTURE\n"I
vcgencmd measure_temp
echo  "\n ${bold} 1. DATE\n"
date
echo  "\n ${bold} 2. IP\n"
hostname -I
echo  "\n ${bold} 3. DISK_VALUE\n"
df -h
echo  "\n ${bold} 4. PORT_CHECK\n"
netstat -an | grep LISTEN
echo  "\n ${bold} 5. /tmp CHECK\n"
ls -al /var/tmp
echo  "\n ${bold} 6. MAIL_IN_QUE\n"
ls -l /var/spool/mqueue | wc -l
echo  "\n ${bold} 7. PSTREE\n"
pstree
echo  "\n ${bold} 8. LAST_LOGIN\n"
lastlog | grep -v "한번도"
echo  "\n ${bold} 9. ROOT_USER_LIST\n"
cat /etc/passwd | grep 0:0
echo  "\n ${bold} 10. MEMORY\n"
free
echo  "\n ${bold} 11. UPTIME\n"
uptime
echo  "\n ${bold} 12. FAIL_LOG\n"
faillog
echo  "\n ${bold} 13. CONNECT_LOG\n"
sudo lastb -10

