# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 00:29:08 2017

@author: mukesh kumar
"""
import webbrowser
import cv2
import numpy as np
from ws4py.client.threadedclient import WebSocketClient
import time, requests
import os
esp8266host = "ws://192.168.43.86:81/"
class DummyClient(WebSocketClient):
    def opened(self):
        print("Websocket open \n")
    def closed(self, code, reason=None):
        print ("Connexion closed down"+code+reason)
    def received_message(self, m):
        print (m)

ws = DummyClient(esp8266host)
ws.connect()       
#import serial
#ser=serial.Serial('com4',115200)
face=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye=cv2.CascadeClassifier('haarcascade_eye.xml')
smile=cv2.CascadeClassifier('haarcascade_smile.xml')
#global flag=0
def detect (gray,frame):
    time.sleep(1)
    #for(x,y,w,h) in face:
    facetuple=face.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in facetuple:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roig=gray[y:y+h,x:x+w]
        roic=frame[y:y+h,x:x+w]
        print ("x"+"="+str(x)+"  "+"y"+"="+str(y)+"h"+"="+str(h))
        if(x>150 and x<300 and y>150 and y<300 ):
            if h>115  and h<150:
                print('o')
                ws.send('o')
                webbrowser.open("https://youtube.com")
                time.sleep(1)
            elif h>0 and h<110:
                print ('b')
                ws.send('2')
                webbrowser.open("https://google.com")
                time.sleep(1)
            elif h>170 and h<300:
                print ('f')
                ws.send('1')
                webbrowser.open("https://twitter.com")
                time.sleep(1)
                
            
        
        elif(x>400 and x<500 and y>150 and y<250):
            print ('4')
            ws.send('l')
            webbrowser.open("https://gmail.com")
            time.sleep(1)
        elif(x>0 and x<100 and y>150 and y<250):
            print ('r')
            ws.send('3')
            webbrowser.open("https://yahoo.com")
            time.sleep(1)
        #elif(x>150 and x<250 and y>150 and y<250 and h):
            #ser.write('f')
        #elif(x>240 and x<270 and y>140 and y<180):
            #ser.write('b')
        #elif(x>240 and x<270 and y>120 and y<130):
            #ser.write('o')
            

        
        
            
        
        
        eyestuple=eye.detectMultiScale(roig,1.1,22)
        for (xx,yy,ww,hh) in eyestuple:
            #print("x"+"="+str(xx)+"  "+"y"+"="+str(yy))
            
            cv2.rectangle(roic,(xx,yy),(xx+ww,yy+hh),(0,255,0),2)
            #roig1=gray[yy:yy+hh,xx:xx+ww]
            #roic1=frame[yy:yy+hh,xx:xx+ww]
            smiletuple=smile.detectMultiScale(roig,1.7,22)
            for (xxx,yyy,www,hhh) in smiletuple:
                
                cv2.rectangle(roic,(xxx,yyy),(xxx+www,yyy+hhh),(0,0,255),2)
                
    return frame

vid=cv2.VideoCapture(0)
while vid.isOpened():
    
    ret,frame=vid.read()
    if ret==1:
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        final=detect(gray,frame)
        cv2.imshow('final',final)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            ws.close()
            break
        
    else:
        break
    
            
vid.release()
cv2.destroyAllWindows()

