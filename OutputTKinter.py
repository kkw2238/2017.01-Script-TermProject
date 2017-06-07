from tkinter import *
from tkinter import font
import getData
import tkinter.messagebox

g_Tk = Tk()
g_Tk.geometry("800x600+100+100")

DataList = []

sidopicks = None
Sidombutton = Menubutton(g_Tk, text= "시/도" )
SidoList = None

stationpicks = None
StationList = []
Stationmbutton = Menubutton(g_Tk, text= "시/도" )

def TKSetting() :
    global SidoList

    SidoList = ["시/도", "서울", "부산", "대구", "인천", "광주", "대전", "울산", "경기", "강원", "충북", "충남", "전북", "전남",
                "경북", "경남", "제주", "세종"]


def SearchLibrary():
    import http.client
    from xml.dom.minidom import parse, parseString

def InitRenderText():
    global RenderText

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
    Sidombutton.place(x = 50 , y = 100)


def SidoSelect(Sido) :

    global SidoList, StationList, stationpicks

    Sidombutton.config(text = SidoList[Sido])

    StationList.clear()

    StationList = getData.GetStationInSidoName(SidoList[Sido])
    StationList.insert(0,"모두")

    for i in range( len(StationList) ):
        Add_Command_Menubutton(i, 1)
    stationpicks.delete(0,stationpicks.size())

##########################################################################


def InitStationSearchMenuButton():

    global Stationmbutton, StationList, stationpicks

    StationSearch = 1

    TempFont = font.Font(g_Tk, size = 15, weight = 'bold', family ='Consolas')

    Stationmbutton = Menubutton(g_Tk, text = "동/리/면")  # the pull-down stands alone

    stationpicks = Menu(Stationmbutton)

    Stationmbutton.config( menu = stationpicks, width = 20, height = 2 )

    if( len(StationList ) == 0 ) :
        pass

    else :
        for i in range(len(StationList) - 1) :
            Add_Command_Menubutton(i, StationSearch)

    print(len(StationList))

    Stationmbutton.pack()

    Stationmbutton.config(bg = 'white', bd = 4, relief = RAISED)

    Stationmbutton.place(x = 300, y = 100)


def StationSelect(Station) :

    global Stationmbutton, SidoList, StationList

    Stationmbutton.config(text = SidoList[Station])

    StationList = getData.GetStationInSidoName(SidoList[Station])

##########################################################################


##########################################################################


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

    TKSetting()
    InitTopText()

    InitSidoSearchMenuButton()
    InitStationSearchMenuButton()

    InitSearchButton()
    InitRenderText()
    g_Tk.mainloop()

main()

