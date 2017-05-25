# -*- coding: cp949 -*-

from http.client import HTTPConnection
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib
import sys

#reload(sys)
#sys.setdefaultencoding('utf-8')

##http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?

##global
conn = None
# regKey = 'z2mxgo5Uk0sWx%2Fchtf0SL2R3i4RnnH4VvlkTtvUwC1ZJYUNKCBu3keO0oBQz9yhg8Tu8q7xpK1JIJ2naACLMiA%3D%3D'

# 네이버 OpenAPI 접속 정보 information
server = "openapi.airkorea.or.kr"

def userURIBuilder(server, **user):
    str = "http://" + server + "/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty" + "?"
    for key in user.keys():
        str += key + "=" + user[key] + "&"
    return str


def connectOpenAPIServer():
    global conn, server
    conn = HTTPConnection(server)

# stationName=종로구&
# dataTerm=month&
# pageNo=1&
# numOfRows=10&
# ServiceKey=z2mxgo5Uk0sWx%2Fchtf0SL2R3i4RnnH4VvlkTtvUwC1ZJYUNKCBu3keO0oBQz9yhg8Tu8q7xpK1JIJ2naACLMiA%3D%3D&
# ver=1.3

def getDataToApi():
    global server, regKey, conn
    if conn == None:
        connectOpenAPIServer()
    uri = userURIBuilder(server, stationName=urllib.parse.quote("종로구"), dataTerm="month", pageNo="1", numOfRows="10",ServiceKey=
    """z2mxgo5Uk0sWx%2Fchtf0SL2R3i4RnnH4VvlkTtvUwC1ZJYUNKCBu3keO0oBQz9yhg8Tu8q7xpK1JIJ2naACLMiA%3D%3D""",ver="1.3")
    print(uri)
    conn.request("GET", uri)
    req = conn.getresponse()
    print(req.status, req.reason)
    print(req.read().decode('utf-8'))

    if int(req.status) == 200:
        print("Data Downloading Complete!")
        return extractBookData(req.read())
    else:
        print("OpenAPI request has been failed!! please retry")
        return None


def extractBookData(strXml):
    from xml.etree import ElementTree
    tree = ElementTree.fromstring(strXml)
    print(strXml)
    # Book 엘리먼트를 가져옵니다.
    itemElements = tree.getiterator("item")  # return list type
    print(itemElements)
    for item in itemElements:
        isbn = item.find("isbn")
        strTitle = item.find("title")
        print(strTitle)
        if len(strTitle.text) > 0:
            return {"ISBN": isbn.text, "title": strTitle.text}


def checkConnection():
    global conn
    if conn == None:
        print("Error : connection is fail")
        return False
    return True

def main() :

    getDataToApi()


main()