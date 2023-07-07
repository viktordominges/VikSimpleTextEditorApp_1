# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 19:20:48 2023

@author: vikto
"""

import PySimpleGUI as sg
import io
import os


scriptPath = os.path.dirname(__file__)
currentFont = 'Arial'
currentSize = 10
firstTimeApp = True
fileName = scriptPath

def about():
    sg.popup('About this program, version 1.0 Beta, Simple Text Editor, Copiright 2023')
    
def save(data):
    if fileName != '':
        with io.open(fileName, 'w', encoding='utf8') as f:
            f.write(data)
        
def save_as(data):
    global fileName
    fileName = sg.tk.filedialog.asksaveasfilename(
        defaultextension = 'txt',
        filetypes = (('All TXT files', '*.txt'), ('All files', '*.*')),
        initialdir = scriptPath,
        title = 'Save As'
        )
    if fileName != '':
        with io.open(fileName, 'w', encoding='utf8') as f:
            f.write(data)

def open_file():
    fileOpen = sg.popup_get_file('file to open', no_window=True)
    if fileOpen != '':
        with open(fileOpen, 'r', encoding='utf8') as f:
            text = f.read()
        window['_text_'].update(value = text)
        window.TKroot.title(fileOpen)

menu = [
        ['File', ['Open', 'Save', 'Save As', 'Close']], 
        ['Edit', ['Font', ['Courier', 'Arial'],'Size', ['10', '12', '14', '16']]], 
        ['About', ['Version']]
        ]

layout = [
    [sg.Menu(menu)],
    [sg.Multiline(size=(600, 400), font=('Arial', 10), key='_text_')]
    ]

window = sg.Window("Simple Text Editor", layout, resizable=True, size = (800, 600), icon='favicon.ico')

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED or event == 'Close':
        break
    
    if event == 'Courier':
        currentFont = 'Courier'
        font = ('Courier', currentSize)
        window['_text_'].update(font = font)
        
    if event == 'Arial':
        currentFont = 'Arial'
        font = ('Arial', currentSize)
        window['_text_'].update(font = font)
        
    if event == '10':
        currentSize = '10'
        font = (currentFont, '10')
        window['_text_'].update(font = font)
        
    if event == '12':
        currentSize = '12'
        font = (currentFont, '12')
        window['_text_'].update(font = font)
        
    if event == '14':
        currentSize = '14'
        font = (currentFont, '14')
        window['_text_'].update(font = font)
        
    if event == '16':
        currentSize = '16'
        font = (currentFont, '16')
        window['_text_'].update(font = font)
        
    if event == 'Version':
        about()
        
    if event == 'Save':
        if firstTimeApp == False:
            save(values['_text_'])
        else:
            save_as(values['_text_'])
            firstTimeApp = False
        
    if event == 'Save As':
        save_as(values['_text_'])
        
    if event == 'Open':
        open_file()
    
window.close()





