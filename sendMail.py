# -*- coding: cp949 -*-
import mimetypes
import mysmtplib
from email.mime.base import MIMEBase
from email.mime.text import MIMEText

#global value
host = "smtp.gmail.com" # Gmail STMP 서버 주소.
port = "587"
htmlFileName = "Data.html"



def SendMail(Datas) :
    global host, port, htmlFileName

    print("메일 보내는 항목입니다. 보내는 사람의 계정 보호를 풀어야 보내질 수 있습니다. ")
    senderAddr = input("보내는 사람의 아이디를 적어주세요 : ")  # 보내는 사람 email 주소.
    senderpass = "rlarjsdn12"
    #senderpass = input("보내는 사람의 비밀번호를 적어주세요 : ")
    recipientAddr = input("받을 사람의 아이디를 적어주세요 : ")  # 받는 사람 email 주소.

    msg = MIMEBase("multipart", "alternative")
    msg['Subject'] = input("제목을 입력해 주세요 : ")  # 내용
    msg['From'] = senderAddr  #
    msg['To'] = recipientAddr

    # MIME 문서를 생성합니다.
    htmlFD = open(htmlFileName, 'rb')
    HtmlPart = MIMEText(Datas, 'html', _charset='UTF-8')
    htmlFD.close()

    # 만들었던 mime을 MIMEBase에 첨부 시킨다.
    msg.attach(HtmlPart)

    # 메일을 발송한다.
    s = mysmtplib.MySMTP(host, port)
    # s.set_debuglevel(1)        # 디버깅이 필요할 경우 주석을 푼다.
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(senderAddr, senderpass)

    try :
        s.sendmail(senderAddr, [recipientAddr], msg.as_string())

    except :
        print("메일 발송에 실패했습니다. https://myaccount.google.com/lesssecureapps?pli=1 에서 계정 보호를 확인해 보거나 ")
        print("메일 아이디 , 비밀번호를 확인해 주세요")
        return None

    else :
        print("메일 발송에 성공했습니다. ")

    s.close()

