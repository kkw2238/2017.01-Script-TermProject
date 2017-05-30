# -*- coding: cp949 -*-
import getData
import getStationData
import sendMail
import ShareFunc

DatasForMail = ""
run = True

def PrintMenu():
    print("----------------------- Menu -----------------------")
    print("S : �õ�, ������ �˻�")
    print("M : ���� �����͸� ���Ϸ� ����")
    print("Q : ������")
    Answer = input("�Է� : ")
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

    SidoList = ["����", "�λ�", "�뱸", "��õ", "����", "����", "���", "���", "����", "���", "�泲", "����", "����",
                "���", "�泲", "����", "����"]

    SidoList.sort()

    print(SidoList)
    Select = input("ã���� �ϴ� ������ ������ �ּ��� : ")

    if Select in SidoList:
        DescriptorMonitoringStation(Select)

    else:
        print("�ٽ� Ȯ���� �ּ���.")


def DescriptorMonitoringStation(Sido):
    MonitoringStation = getData.GetStationInSidoName(Sido)
    MonitoringStation.append("���")

    Page = 1
    Again = True
    Description = True
    Data = []

    while( Description ) :
        Again = True

        print(MonitoringStation)
        Select = input("�ڼ��� ����� ���ϴ� �����Ҹ� �Է��� �ּ��� : ")

        while(Again) :

            if( Select in MonitoringStation) :
                if (Select == "���"):
                    (Data, Continue) = getData.getSidoDataToApi("All", Sido, Page)

                else :
                    (Data, Continue) = getStationData.getStationDataToApi("All", Select, Page)

            else :
                print("�Է��� Ȯ���� �ּ��� ")
                Again = False
                break

            PrintData(Data)

            if Data != None and Continue:
                NextPage = input("���� �������� ��� �Ͻðڽ��ϱ�?(Y/N) : ")

                if NextPage == "Y":
                    Page += 1

                else:
                    Again = False
                    Description = False

            elif not Continue:
                print("�����Ͱ� �� �̻� �����ϴ�.")
                Again = False
                Description = False

main()