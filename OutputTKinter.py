from tkinter import *
from tkinter import font
import getData
import getStationData
import ShareFunc

import tkinter.messagebox

g_Tk = Tk()
g_Tk.geometry("800x600+100+100")

RenderData = None

selectSido = None
sidopicks = None
Sidombutton = Menubutton(g_Tk, text= "시/도" )
SidoList = None

stationpicks = None
StationList = []
Stationmbutton = Menubutton(g_Tk, text= "시/도" )

Data = None

State = 1



def TKSetting() :
    global SidoList

    SidoList = ["시/도", "서울", "부산", "대구", "인천", "광주", "대전", "울산", "경기", "강원", "충북", "충남", "전북", "전남",
                "경북", "경남", "제주", "세종"]


def SearchLibrary():
    import http.client
    from xml.dom.minidom import parse, parseString


def SearchButtonAction():
    global SearchListBox

def InitSearchButton():
    pass


##########################################################################
# 시/도 정보를 메뉴 버튼 방식으로 보여준다.
def InitSidoSearchMenuButton():

    global Sidombutton, SidoList, sidopicks

    SidoSearch = 0

    TempFont = font.Font(g_Tk, size = 15, weight = 'bold', family ='Consolas')

    Sidombutton = Menubutton(g_Tk, text = "시/도" , direction = LEFT)  # the pull-down stands alone

    sidopicks = Menu(Sidombutton)

    Sidombutton.config(menu = sidopicks, width = 20, height = 2)

    for i in range(len(SidoList) - 1) :
        Add_Command_Menubutton(i, SidoSearch)

    Sidombutton.pack()

    Sidombutton.config(bg = 'white', bd = 4, relief = RAISED)
    Sidombutton.place(x = 25 , y = 150)


def SidoSelect(Sido) :

    global SidoList, StationList, stationpicks, selectSido

    Sidombutton.config(text = SidoList[Sido])
    selectSido = SidoList[Sido]

    if StationList :
        for i in range(len(StationList)) :
            stationpicks.delete(StationList[i])

    StationList.clear()

    StationList = getData.GetStationInSidoName(SidoList[Sido])
    StationList.insert(0,"모두")

    for i in range( len(StationList) ):
        Add_Command_Menubutton(i, 1)

##########################################################################


def InitStationSearchMenuButton():

    global Stationmbutton, StationList, stationpicks

    StationSearch = 1

    TempFont = font.Font(g_Tk, size = 15, weight = 'bold', family ='Consolas')

    Stationmbutton = Menubutton(g_Tk, text = "동/리/면")  # the pull-down stands alone

    stationpicks = Menu(Stationmbutton)

    Stationmbutton.config( menu = stationpicks, width = 20, height = 2 )

    if( len( StationList ) == 0 ) :
        pass

    else :
        for i in range(len(StationList) - 1) :
            Add_Command_Menubutton(i, StationSearch)

    print(len(StationList))

    Stationmbutton.pack()

    Stationmbutton.config(bg = 'white', bd = 4, relief = RAISED)

    Stationmbutton.place(x = 200, y = 150)


def StationSelect(Station) :

    global Stationmbutton, SidoList, StationList, selectSido, Data, RenderData

    Stationmbutton.config(text = StationList[Station])

    if( StationList[Station] == "모두") :
        StationList = getData.getSidoDataToApi("ALL", selectSido , 1 )

    else:
        (Data, Continue) = getStationData.getStationDataToApi("All", StationList[Station], 1)

    RenderData.configure(state='normal')
    RenderData.delete(0.0, END)
    RenderData.insert(INSERT, ShareFunc.PrintData(Data, selectSido, StationList[Station], 0))
##########################################################################


def InitRenderText():
    global RenderData

    TextScrollbar = Scrollbar(g_Tk)
    TextScrollbar.pack()
    TextScrollbar.place(x = 375, y = 200)

    Font = font.Font(g_Tk, size = 12, family = "Consolas")
    RenderData = Text(g_Tk, width = 49, height = 27, borderwidth = 12,
                relief = 'ridge', yscrollcommand = TextScrollbar.set)
    RenderData.pack()
    RenderData.place(x = 10, y = 215)
    TextScrollbar.config(command = RenderData.yview)
    TextScrollbar.pack(side = RIGHT, fill = BOTH)

    RenderData.configure(state = "disabled")


##########################################################################


def InitHelp():
    TextScrollbar = Scrollbar(g_Tk)
    TextScrollbar.pack()
    TextScrollbar.place(x=375, y=200)

    Font = font.Font(g_Tk, size = 12, family = "Consolas")
    RenderHelp = Text(g_Tk, width = 110, height = 43, borderwidth = 12,
                relief = 'ridge', yscrollcommand = TextScrollbar.set)
    RenderHelp.configure(state='normal')
    RenderHelp.delete(0.0, END)
    RenderHelp.insert(INSERT, "도움말")

    RenderHelp.pack()
    RenderHelp.place(x = 0, y = 0)
    TextScrollbar.config(command = RenderHelp.yview)
    TextScrollbar.pack(side = RIGHT, fill = BOTH)

    RenderHelp.configure(state = "disabled")

##########################################################################
def Add_Command_Menubutton(j, Type):
    global SidoList, StationList, stationpicks , sidopicks

    if Type is 0:
        sidopicks.add_command(label = SidoList[j + 1], command = lambda: SidoSelect(j + 1) )

    if Type is 1:
        stationpicks.add_command(label = StationList[j], command = lambda : StationSelect( j ) )

def InitTopText():
    pass

def main() :
    global State

    TKSetting()
    InitTopText()

    InitSidoSearchMenuButton()
    InitStationSearchMenuButton()

    InitSearchButton()

    if State == 0 :
        InitRenderText()
    else :
        InitHelp()

    g_Tk.mainloop()

main()

