# -*- coding: utf-8 -*-
#! Python3

import os

def write_memo():
    print('메모 프로그램 입니다. 날자를 입력해 주세요.')
    day = input('YYMMDD:')
    print('별표(*) 3개 입력시 메모입력이 종료됩니다.')

# mailbox 디렉토리로 이동.
    os.chdir('/home/pi/mygit/R-pi/memo/mailbox')

# 날자를 입력받아 그 날자를 파일명으로 open.
    file_name = ('%s.txt' % day)
    memo_file = open(file_name ,'a')

# '***'입력시 프로그램이 종료되도록. 입력값이 한줄씩 저장되도록 \n 추가.
    while True:
        put = input()
        if put == '***':
            break
        memo_file.writelines(put+'\n')
    memo_file.close()

if __name__ == '__main__':
    write_memo()

