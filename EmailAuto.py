# 이메일 메시지에 다양한 형식을 중첩하여 담기 위한 객체
import smtplib

# 텍스트 형식
from email.mime.text import MIMEText


smtp_info=dict({"smtp_server" : "smtp.naver.com", # SMTP 서버 주소
                  "smtp_user_id" : "<보내는 사람의 이메일 주소>", 
                  "smtp_user_pw" : "<보내는 사람의 이메일 비밀번호>" ,
                  "smtp_port" : 587}) # SMTP 서버 포트


# 메일 전송을 위한 함수
def send_email(smtp_info, msg):
    with smtplib.SMTP(smtp_info["smtp_server"], smtp_info["smtp_port"]) as server:
        # TLS 보안 연결
        server.starttls() 
        # 로그인
        server.login(smtp_info["smtp_user_id"], smtp_info["smtp_user_pw"])

        # 로그인 된 서버에 이메일 전송
        response = server.sendmail(msg['from'], msg['to'], msg.as_string()) # 메시지를 보낼때는 .as_string() 메소드를 사용해서 문자열로 바꿔줍니다.

        # 이메일을 성공적으로 보내면 결과는 {}
        if not response:
            print('이메일을 성공적으로 보냈습니다.')
        else:
            print(response)


# 메일 내용 작성
title = "타이틀" 
content = ""
sender = "<보내는 사람의 이메일>"
receiver = "email@naver.com" #받는 사람의 이메일

# 메일 객체 생성 : 메시지 내용에는 한글이 들어가기 때문에 한글을 지원하는 문자 체계인 UTF-8을 명시해줍니다.
msg = MIMEText(_text = content, _charset = "utf-8") # 메일 내용

msg['Subject'] = title     # 메일 제목
msg['From'] = sender       # 송신자
msg['To'] = receiver       # 수신자


#send_email(smtp_info, msg )
