# -*- coding: cp949 -*-
import mimetypes
import mysmtplib
from email.mime.base import MIMEBase
from email.mime.text import MIMEText

#global value
host = "smtp.gmail.com" # Gmail STMP ���� �ּ�.
port = "587"
htmlFileName = "Data.html"



def SendMail(Datas) :
    global host, port, htmlFileName

    print("���� ������ �׸��Դϴ�. ������ ����� ���� ��ȣ�� Ǯ��� ������ �� �ֽ��ϴ�. ")
    senderAddr = input("������ ����� ���̵� �����ּ��� : ")  # ������ ��� email �ּ�.
    senderpass = "rlarjsdn12"
    #senderpass = input("������ ����� ��й�ȣ�� �����ּ��� : ")
    recipientAddr = input("���� ����� ���̵� �����ּ��� : ")  # �޴� ��� email �ּ�.

    msg = MIMEBase("multipart", "alternative")
    msg['Subject'] = input("������ �Է��� �ּ��� : ")  # ����
    msg['From'] = senderAddr  #
    msg['To'] = recipientAddr

    # MIME ������ �����մϴ�.
    htmlFD = open(htmlFileName, 'rb')
    HtmlPart = MIMEText(Datas, 'html', _charset='UTF-8')
    htmlFD.close()

    # ������� mime�� MIMEBase�� ÷�� ��Ų��.
    msg.attach(HtmlPart)

    # ������ �߼��Ѵ�.
    s = mysmtplib.MySMTP(host, port)
    # s.set_debuglevel(1)        # ������� �ʿ��� ��� �ּ��� Ǭ��.
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(senderAddr, senderpass)

    try :
        s.sendmail(senderAddr, [recipientAddr], msg.as_string())

    except :
        print("���� �߼ۿ� �����߽��ϴ�. https://myaccount.google.com/lesssecureapps?pli=1 ���� ���� ��ȣ�� Ȯ���� ���ų� ")
        print("���� ���̵� , ��й�ȣ�� Ȯ���� �ּ���")
        return None

    else :
        print("���� �߼ۿ� �����߽��ϴ�. ")

    s.close()

