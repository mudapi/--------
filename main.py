import PySimpleGUI as sg
import time

sg.theme('DarkBlack')
layout_main = [

    [sg.B('配置')],[sg.B('关闭')]
]#设置窗口元素

windows_main = sg.Window('记录仪自动导入程序',layout_main,keep_on_top=1,icon='./1.ico')   #显示窗口
#config.ini
配置窗口 = 0

while True:   #设置窗口循环
    event_main,values_main = windows_main.read()   #设置变量作为窗口显示内容
    if event_main in (None,'关闭'):
        break
    if 配置窗口==0 and event_main=='配置':
        配置窗口 = 1
        layout_config = [
            [sg.B('配置')],[sg.B('关闭')]
            ]
        windows_config = sg.Window('配置程序',layout_config,keep_on_top=1,icon='./1.ico')
    if 配置窗口==1:
        event_config,values_config = windows_config.read()
        if event_config in (None,'关闭'):
            break
        
