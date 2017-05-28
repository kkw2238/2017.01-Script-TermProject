# -*- coding: cp949 -*-
import urllib
import ShareFunc

StationList = []

def getSidoDataToApi(Type, Sido, Page):

    Conn = ShareFunc.Conn
    Server = "openapi.airkorea.or.kr"

    if Conn == None:
        Conn = ShareFunc.connectOpenAPIServer()

    uri = ShareFunc.userURIBuilder(Server, 1 , sidoName=urllib.parse.quote(Sido), pageNo="{0}".format(Page), numOfRows="10",ServiceKey=
    """z2mxgo5Uk0sWx%2Fchtf0SL2R3i4RnnH4VvlkTtvUwC1ZJYUNKCBu3keO0oBQz9yhg8Tu8q7xpK1JIJ2naACLMiA%3D%3D""",ver="1.3")

    print(uri)
    Conn.request("GET", uri)
    req = Conn.getresponse()

    if int(req.status) == 200:
        print("Data Downloading Complete!")

        tmp , DataCount = ShareFunc.extractParseData(req.read().decode('utf-8'), Type, 1)

        Continue = not (DataCount < 10)

        return tmp , Continue

    else:
        print("OpenAPI request has been failed!! please retry")
        return None


def GetStationInSidoName(Sido) :                      # StationList�� ����� ��ȯ�Ѵ�.

    Page = 1
    SearchAgain = True

    StationList = []

    while ( SearchAgain ) :
        tmp , Continue = getSidoDataToApi("StationOnly", Sido, Page)

        if tmp is not None :
            StationList += tmp

        if( not Continue ) :
            SearchAgain = False

        else :
            Page += 1

    return StationList


# ����, �λ�, �뱸, ��õ, ����, ����, ���, ���, ����, ���, �泲, ����, ����, ���, �泲, ����, ����
