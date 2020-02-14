#!/usr/bin/env python

import subprocess
from tkinter import *

ipAddress = {'google': '8.8.8.8',
             'yahoo': '75.75.75.75',
             'home': '192.168.0.1',
             'test': '123.2.4.32',
             'raleigh': '192.168.2.1',
             'bartow': '192.168.4.1',
             'stuart': '192.168.5.1',
             'chandler mtn fs': '192.168.6.1',
             'cheriton': '192.168.8.1',
             'parksley': '192.168.9.1',
             'bailey': '192.168.11.1',
             'faison': '192.168.12.1',
             'fountain': '192.168.13.1',
             'wilson': '192.168.15.1',
             'clayton': '192.168.16.1',
             'bladen': '192.168.17.1',
             'Palm View': '192.168.18.1',
             'washington':	'192.168.19.1',
             'bowling green': '192.168.20.1',
             'ft meade': '192.168.21.1',
             'ft pierce': '192.168.22.1',
             'indiantown': '192.168.23.1',
             'jennings': '192.168.24.1',
             'la Familia': '192.168.25.1',
             'okee1': '192.168.26.1',
             'okee2': '192.168.27.1',
             'shannon': '192.168.28.1',
             'south bay': '192.168.29.1',
             'chandler mtn': '192.168.31.1',
             'okee trans': '192.168.32.1',
             'semmes': '192.168.33.1',
             'loxley': '192.168.34.1',
             'myakka': '192.168.35.1',
             'mobile': '192.168.36.1',
             'chandler mtn trans': '192.168.37.1',
             'charleston': '192.168.38.1',
             'colleton': '192.168.39.1',
             'wauchula trans': '192.168.41.1',
             'manning':	'192.168.42.1',
             'semmes trans': '192.168.43.1',
             'manning trans': '192.168.44.1',
             'colleton trans': '192.168.45.1',
             'wauchula': '192.168.30.1',
             'angier': '10.100.10.1',
             'newton grove': '10.101.10.1',
             'whiteville': '10.102.10.1',
             'hendersonville': '10.103.10.1',
             'gaffney': '10.104.10.1',
             'oneonta': '10.105.10.1'
}


master = Tk()


lbl2 = Label(master, text=" ")


def pingIP():
    center = entry.get().lower()
    for key, value in ipAddress.items():
        if center == key:
            response = subprocess.call(['ping', '-n', '1', value])
            if response == 0:
                result = key.upper() + ' is up!'
                lbl2.configure(text=result, bg='green')
                lbl2.update_idletasks()
                lbl2.place(x=140, y=170)
            else:
                result = key.upper() + ' is down!'
                lbl2.configure(text=result, bg='red')
                lbl2.update_idletasks()


quitButton = Button(master, text="Quit", command=quit, highlightbackground='#adadac')
quitButton.place(x=0, y=0)
submitButton = Button(master, text="PING", command=pingIP, highlightbackground='blue').place(x=200, y=120)
lbl = Label(master, text="Enter center name: ").place(x=20, y=90)

entry = Entry(master, bd=2)
entry.place(x=150, y=87)
master.title("PING IP")
master.geometry("400x250")
mainloop()
