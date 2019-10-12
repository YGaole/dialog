# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 13:05:26 2019

@author: rt123
"""
import codecs
import datetime
ntime = datetime.datetime.now().strftime('%Y-%m-%d')
f=codecs.open('everydaytask','r','utf-8')
date=f.readlines()
f.close()
ttime=date[0].split(':')
a=[int(i) for i in ttime[0].split('-')]
b=[int(i) for i in ntime.split('-')]
if a!=b:
    print('add:\n')
    date[0]=ntime+':'+ttime[1]
    f=codecs.open('everydaytask','w','utf-8')
    for i in date:
        f.write(i)
    f.close()
    dat=codecs.open('Dialog.todo','r','utf-8')
    dat.seek(-2,2)
    if dat.read()!='\r\n':
        date[0]='\r\n'+ntime+':'+ttime[1]
    dat.close()
    dat=codecs.open('Dialog.todo','a+','utf-8')
    for i in date:
        dat.write(i)
        print(i)
    dat.close()