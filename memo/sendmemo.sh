#!/bin/sh

# mailbox 디렉토리 아래에 확장자가 txt인 파일이 있으면~
memofile=`find /home/pi/memo/mailbox -type f -name *.txt`

# 메일을 보내고, 없다면 메세지 띄운후 종료.
# 파일은 메일을 보낸 후 sended_memo 디렉토리로 옮긴다.
# 파일이 여러개 일때 하나하나 보낸다!
if [ "$memofile" ];then
    for files in $memofile
    do
        /usr/sbin/ssmtp kj2693119@gmail.com < $files
    done
    cd mailbox/
    mv *.txt ../sended_memo
else
   echo "더이상 보낼 메모가 없습니다." 
fi

