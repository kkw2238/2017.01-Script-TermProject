
from http.client import HTTPConnection
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib
import sys


Conn = None
StationList = []
Server = "openapi.airkorea.or.kr"
Service = ["getMsrstnAcctoRltmMesureDnsty" , "getCtprvnRltmMesureDnsty"]
#getMsrstnAcctoRltmMesureDnsty  측정소별
#getCtprvnRltmMesureDnsty       시 , 도별

def connectOpenAPIServer():
    global Server, Conn

    Conn = HTTPConnection(Server)
    return Conn


def userURIBuilder(server, service , **user):
    global Service

    str = "http://" + server + "/openapi/services/rest/ArpltnInforInqireSvc/" + Service[service] + "?"

    for key in user.keys():
        str += key + "=" + user[key] + "&"

    return str


# 입력받은 시간 값을 문자열로 년 , 월 , 일이 추가된 문자열로 바꿔준다.
def MakeaStringtoTime(Time) :

    YMDCount = 0
    YMD = [ "년 " , "월 " , "일 " ]
    String = ""

    for Char in Time :

        if (Char == '-') or (Char == " ")  :
            String += YMD[ YMDCount ]
            YMDCount += 1

        else :
            String += Char

    return String

# Parsing Data를 얻어준다.
def extractParseData(strXml, Type, Service):
    from xml.etree import ElementTree

    tree = ElementTree.fromstring(strXml)

    # tree.getiterator("items") : 파싱 결과에서 items에 속한 요소를 List로 묶어서 보내준다.
    # 현재 상태 Datas[items[(item(stationName ...), item(stationName ...) , ...)]]
    DataList , DataCount = ElementtoList(tree.getiterator("items"), Type, Service)

    return DataList , DataCount


# 파싱해온 데이터를 List로 만들어준다.
def ElementtoList(itemElements, Type, Service) :

    List = []

    DataCount = 0

    # 현재 상태 Datas[items[item(stationName ...), item(stationName ...) , ...)]]
    # Datas(itemElements)에서 items를 1개씩 꺼낸다.
    for item in itemElements:

        # items에 있는 item을 꺼낸다.
        for Data in item :

            Dic = {}

            # item에 있는 Data내용을 찾는다.
            if Service == 1 :
                stationName = Data.find("stationName")

                # .text : 데이터 내부 <stationName> text </stationName>의 text를 꺼내온다.
                Dic["지역 : "] = stationName.text

                if (Type == "StationOnly"):
                    List.append(stationName.text)
                    DataCount += 1
                    continue

            # 이하 동문
            dataTime = MakeaStringtoTime(Data.find("dataTime").text)  # 측정 시간
            coValue = Data.find("coValue")  # 일산화 탄소 농도
            pm10Value = Data.find("pm10Value")  # 미세먼지 농도
            o3Value = Data.find("o3Value")  # 오존 농도
            pm10Grade = Data.find("pm10Grade")  # 미세먼지 등급
            khaiGrade = Data.find("khaiGrade")  # 종합 등급

            # 데이터가 없지 않으면 Dict형식으로 만들어 저장하고
            if Data is not None :
                Dic.update( {"측정 시간 : ": dataTime,
                        "일산화 탄소 농도 : ": coValue.text,
                        "미세먼지 농도 : ": pm10Value.text,
                        "오존 농도 : ": o3Value.text,
                        "미세먼지 등급 : ": pm10Grade.text,
                        "종합 등급 : ": khaiGrade.text
                        })

                # 리스트에 넣어준다.
                List.append(Dic)

            DataCount += 1

        return List , DataCount

def Quit() :
    global Conn

    if Conn != None :
        Conn.close()



######################################################


def PrintData(Datas, Sido, Selected, Type) :

    if (Datas == None ) :
        return None

    DatasForMail = ""
    StringData = ""

    if Selected != None :
        DatasForMail += ( Sido + " " + Selected + "측정소 결과 데이터 입니다.<br>" )
        StringData += ( Sido + " " + Selected + """측정소 결과 데이터 입니다.

""" )

    else :
        DatasForMail += (Sido + "에 위치한 각 측정소 결과 데이터 입니다.<br>")
        StringData += (Sido + """에 위치한 각 측정소 결과 데이터 입니다.
""")

    for Data in Datas :
        for item in Data.items() :
            key , value = item

            if value == None :
                DatasForMail += (key + "알 수 없음" + "<br>")
                StringData += (key + """알 수 없음

""")
                continue

            DatasForMail += (key + value + "<br>" )
            StringData += (key + value + """

""")

        DatasForMail += "<br>"
        StringData += """

"""

    if Type == 0 :
        return StringData

    else :
        return DatasForMail