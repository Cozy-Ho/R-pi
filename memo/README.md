# 메일 알림 메모장

- 주말을 지나면서 계획했던 것들을 까먹는 경우를 줄이고자 만듦.
- `crontab`에 올려서 매 주 금요일, 메모 내용들을 긁어 보냄.
- 중복된 알림을 방지하기위해 메일 발송이 끝난 메모들은 따로 보관.

## 사용법
1. memo 디렉토리를 다운로드한다.
2. sendmemo.sh 파일의 디렉토리 경로명을 본인의 디렉토리에 맞게 수정한다.
3. crontab 에는 sendmemo.sh 파일만 올려놓는다.
4. 메모를 할때는 main.py 를 실행시켜 메모한다.

