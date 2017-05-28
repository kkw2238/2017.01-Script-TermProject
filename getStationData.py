import urllib
import ShareFunc

StationList = []

def getStationDataToApi(Type, Stage, Page):

    Conn = ShareFunc.Conn
    Server = "openapi.airkorea.or.kr"

    if Conn == None:
        Conn = ShareFunc.connectOpenAPIServer()

    uri = ShareFunc.userURIBuilder(Server, 0 , stationName=urllib.parse.quote(Stage), pageNo="{0}".format(Page), numOfRows="10",
                                   dataTerm="month",ServiceKey =
    """z2mxgo5Uk0sWx%2Fchtf0SL2R3i4RnnH4VvlkTtvUwC1ZJYUNKCBu3keO0oBQz9yhg8Tu8q7xpK1JIJ2naACLMiA%3D%3D""",ver="1.3")

    print(uri)
    Conn.request("GET", uri)
    req = Conn.getresponse()

    if int(req.status) == 200:
        print("Data Downloading Complete!")

        tmp , DataCount = ShareFunc.extractParseData(req.read().decode('utf-8'), Type, 0)

        Continue = not (DataCount < 10)

        return tmp , Continue

    else:
        print("OpenAPI request has been failed!! please retry")
        return None


# 서울, 부산, 대구, 인천, 광주, 대전, 울산, 경기, 강원, 충북, 충남, 전북, 전남, 경북, 경남, 제주, 세종