import PySimpleGUI as sg
import os

sg.theme('DarkBlack')
配置 = sg.UserSettings(filename='config.json',path='.',use_config_file=False)
layout = [
    [sg.Text('视频所在文件夹'),sg.Input(配置['视频所在路径'],k='视频所在路径',enable_events=True),sg.FolderBrowse('选择')],
    [sg.Text('视频保存到'),sg.Input(配置['视频保存路径'],k='视频保存路径',enable_events=True),sg.FolderBrowse('选择')],
    
    [sg.Text('要保存的文件类项')],
    [sg.FileBrowse('类项1',target='保存1'),sg.Input(配置['保存1'],s=4,k='保存1',enable_events=True),
    sg.FilesBrowse('类项2',target='保存2'),sg.Input(配置['保存2'],s=4,k='保存2',enable_events=True),
    sg.FilesBrowse('类项3',target='保存3'),sg.Input(配置['保存3'],s=4,k='保存3',enable_events=True),
    sg.FilesBrowse('类项4',target='保存4'),sg.Input(配置['保存4'],s=4,k='保存4',enable_events=True)],
    [sg.Text('要删除的文件类项')],
    [sg.FileBrowse('类项1',target='删除1'),sg.Input(配置['删除1'],s=4,k='删除1',enable_events=True),
    sg.FilesBrowse('类项2',target='删除2'),sg.Input(配置['删除2'],s=4,k='删除2',enable_events=True),
    sg.FilesBrowse('类项3',target='删除3'),sg.Input(配置['删除3'],s=4,k='删除3',enable_events=True),
    sg.FilesBrowse('类项4',target='删除4'),sg.Input(配置['删除4'],s=4,k='删除4',enable_events=True)],
    [sg.Text('',k='反馈'),sg.Text('00',text_color='#2C2C2C',justification='right',expand_x=True)],
    [sg.B('保存配置'),sg.B('加载'),sg.B('关闭'),sg.Text('17859951771',text_color='#2C2C2C',justification='right',expand_x=True,p=(12,0))]
]

windows_config = sg.Window('配置程序',layout,keep_on_top=1,icon='./1.ico')   #显示窗口
#config.ini

while True:   #设置窗口循环
    event_config,values_config = windows_config.read()   #设置变量作为窗口显示内容
    if event_config in (None,'关闭'):
        break
    if event_config in ('视频所在路径','视频保存路径','保存1','保存2','保存3','保存4','删除1','删除2','删除3','删除4'):
        windows_config[event_config].update(os.path.splitext(values_config[event_config])[1])
        配置[event_config]=(os.path.splitext(values_config[event_config])[1])
    if event_config=='保存配置':
        配置.save()
        windows_config['反馈'].update(f'配置保存到  {配置.full_filename}')
    if event_config=='加载':
        配置.read()
        for i in ('视频所在路径','视频保存路径','保存1','保存2','保存3','保存4','删除1','删除2','删除3','删除4'):
            windows_config[i].update(配置[i])
        windows_config['反馈'].update(f'从  {配置.full_filename}  读取配置')
    
    