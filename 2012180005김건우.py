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
        DatasForMail += ( Sido + " " + Selected + "������ ��� ������ �Դϴ�.<br>" )
        StringData += ( Sido + " " + Selected + """������ ��� ������ �Դϴ�.
""" )

    else :
        DatasForMail += (Sido + "�� ��ġ�� �� ������ ��� ������ �Դϴ�.<br>")
        StringData += (Sido + """�� ��ġ�� �� ������ ��� ������ �Դϴ�.
""")

    for Data in Datas :
        for item in Data.items() :
            key , value = item

            if value == None :
                DatasForMail += (key + "�� �� ����" + "<br>")
                StringData += (key + """�� �� ����
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
                    PrintData(Data, Sido, None)

                else :
                    (Data, Continue) = getStationData.getStationDataToApi("All", Select, Page)
                    PrintData(Data, Sido, Select)

            else :
                print("�Է��� Ȯ���� �ּ��� ")
                Again = False
                break



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
