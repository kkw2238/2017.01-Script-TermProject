# -*- coding: cp949 -*-
import getData
import getStationData
import sendMail
import ShareFunc

DatasForMail = ""
run = True

def PrintMenu():
    print("----------------------- Menu -----------------------")
    print("S : 시도, 측정소 검색")
    print("M : 현재 데이터를 메일로 전송")
    print("Q : 나가기")
    Answer = input("입력 : ")
    InputMenu(Answer)

def InputMenu(Answer) :
    global run, DatasForMail

    if Answer is "S" :
        SearchData()

    elif Answer is "M" :
        sendMail.SendMail(DatasForMail)

    elif Answer is "Q" :
        run = False

        ShareFunc.Quit()


def PrintData(Datas) :
    global DatasForMail

    StringData = ""

    for Data in Datas :
        for item in Data.items() :
            key , value = item
            DatasForMail += (key + value + "<br>" )
            StringData += (key + value + """
""")

        DatasForMail += "<br>"
        StringData += """
"""

    print(StringData)

def main() :
    global run

    while(run) :
        PrintMenu()

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

                else :
                    (Data, Continue) = getStationData.getStationDataToApi("All", Select, Page)

            else :
                print("입력을 확인해 주세요 ")
                Again = False
                break

            PrintData(Data)

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

main()