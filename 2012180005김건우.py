# -*- coding: cp949 -*-
import getData
import getStationData
import sendMail

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

def PrintData(Datas) :
    global DatasForMail
    for Data in Datas :
        print(Data)
        DatasForMail += Data.__str__() + "�n"

    print(DatasForMail)

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
    Data = []

    print(MonitoringStation)
    Select = input("�ڼ��� ����� ���ϴ� �����Ҹ� �Է��� �ּ��� : ")

    while(Again) :

        if( Select == "���" ) :
            (Data , Continue) = getData.getSidoDataToApi("All", Sido, Page)
            PrintData(Data)

        elif( Select in MonitoringStation) :
            (Data, Continue) = getStationData.getStationDataToApi("All", Select, Page)

        PrintData(Data)

        if Data != None and Continue:
            NextPage = input("���� �������� ��� �Ͻðڽ��ϱ�?(Y/N) : ")

            if NextPage == "Y":
                Page += 1

            else:
                Again = False

        elif not Continue:
            print("�����Ͱ� �� �̻� �����ϴ�.")
            Again = False

main()