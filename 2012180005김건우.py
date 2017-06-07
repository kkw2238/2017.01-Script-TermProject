# -*- coding: cp949 -*-
import getData
import getStationData
import sendMail
import ShareFunc
import tkinter

DatasForMail = ""
run = True

def InputMenu(Answer) :
    global run, DatasForMail

    if Answer is "S" :
        SearchData()

    elif Answer is "M" :
        sendMail.SendMail(DatasForMail)

    elif Answer is "Q" :
        run = False

        ShareFunc.Quit()


def PrintData(Datas, Sido, Selected) :
    global DatasForMail

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

    print(StringData)

def SearchData() :
    global run

    SidoList = ["서울", "부산", "대구", "인천", "광주", "대전", "울산", "경기", "강원", "충북", "충남", "전북", "전남",
                "경북", "경남", "제주", "세종"]

    SidoList.sort()

    print(SidoList)
    Select = input("찾고자 하는 지역을 선택해 주세요 : ")

    if Select in SidoList:
        DescriptorMonitoringStation(Select)

    else:
        print("다시 확인해 주세요.")


def DescriptorMonitoringStation(Sido):
    MonitoringStation = getData.GetStationInSidoName(Sido)
    MonitoringStation.append("모두")

    Page = 1
    Again = True
    Description = True
    Data = []

    while( Description ) :
        Again = True

        print(MonitoringStation)
        Select = input("자세한 결과를 원하는 측정소를 입력해 주세요 : ")

        while(Again) :

            if( Select in MonitoringStation) :
                if (Select == "모두"):
                    (Data, Continue) = getData.getSidoDataToApi("All", Sido, Page)
                    PrintData(Data, Sido, None)

                else :
                    (Data, Continue) = getStationData.getStationDataToApi("All", Select, Page)
                    PrintData(Data, Sido, Select)

            else :
                print("입력을 확인해 주세요 ")
                Again = False
                break



            if Data != None and Continue:
                NextPage = input("다음 페이지를 출력 하시겠습니까?(Y/N) : ")

                if NextPage == "Y":
                    Page += 1

                else:
                    Again = False
                    Description = False

            elif not Continue:
                print("데이터가 더 이상 없습니다.")
                Again = False
                Description = False
