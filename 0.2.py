#!/usr/bin/python3
#-*-coding:utf-8-*-

from urllib import request as req
import urllib
from sys import argv
import datetime

# Verfügbare Stationen: 
#    Zwinglistraße    - Code: ZWI
#    Schneebergstraße - Code. SNS
# Verfügbare Linien [Linie (Code)]:
# SNS: 61 (61 19 67 08)
#      85 (voe%3a21085%3a+%3aH%3aj16)
#      64 (61 19 76 82)
# ZWI:  1 (61 19 09 70)
#       2 (61 19 26 34)

def get01(station, linie):
    d = datetime.datetime.now()
    zeit = d.strftime("%H:%M")
    zeit = zeit.replace(":","%3a")
    datum = d.strftime("%d.%m.%Y")

    if station == "ZWI" and ( linie == "61" or linie == "64" or linie == "85"):
        print("Zwinglistraße nur für 1 und 2")
        exit()
    elif station == "SNS" and ( linie == "1" or linie == "2" ):
        print("Schneebergstraße nur für 61, 64 und 85")
        exit()

    stopID = ""
    if station == "ZWI":
        stopID = "33000084" #ZWI
    elif station == "SNS":
        stopID = "33000819" #SNS
    else:
        print("Keine gültige Haltestelle!")
        exit()
        
    departureID = ""
    if linie == "61":
        departureID = "61196708"
    elif linie == "64":
        departureID = "61197682"
    elif linie == "85":
        departureID = "61217783"
    elif linie == "1":
        departureID = "61190970"
    elif linie == "2":
        departureID = "61192634"
    else:
        print("Keine gültige Liniennummer!")
        exit()

    url = "https://www.dvb.de/de-de/apps/StopInformation?stopid=" + stopID + "&date=" + datum + "&time=" + zeit + "&arrival=False&mot=Tram&mot=CityBus&departureid=" + departureID + "&timetables=False&submit=true"

    text = ""
    with req.urlopen(url) as response:
        for line in response:
            line = line.decode('utf-8')
            text += line
    
    saveFile = open("testX.txt", 'w')
    saveFile.write(text)
    saveFile.close()

    outFile = open(haltestelle+".txt", 'w')
    outTxt = []
    txtIndex = text.find("c3of15")
    while txtIndex != -1:
        text = text[txtIndex+6:]
        tmp = text.find("strong")
        text = text[tmp+7:]
        tmp1 = text[:text.find("<")]
        tmp = text.find("c8of15")
        text = text[tmp+6:]
        tmp = text.find("strong")
        text = text[tmp+7:]
        tmp2 = text[:text.find("<")]
        tmp2 = tmp2.replace("&#252;","ü")
        tmp2 = tmp2.replace("&#246;","ö")
        tmp2 = tmp2.replace("&#228;","ä")
        tmp2 = tmp2.replace("&#223;","ß")
        tmp = text.find("late")
        tmp4 = "NULL"
        if tmp != -1 and tmp < 200:
            tmp4 = text[tmp:]
            tmp4 = tmp4[tmp4.find("+"):]
            tmp4 = tmp4[:tmp4.find("\n")]
        tmp = text.find("c4of15")
        text = text[tmp+6:]
        tmp = text.find("strong")
        text = text[tmp+7:]
        tmp3 = text[:text.find("<")]
        if tmp1.find("Linien") == -1:
            if tmp4 != "NULL":
                outFile.write(tmp1 + "\t" + tmp2 + "\t" + tmp3 + "\t" + tmp4 + "\n")
            else:
                outFile.write(tmp1 + "\t" + tmp2 + "\t" + tmp3 + "\n")

        txtIndex = text.find("cols15")
    
    outFile.close()



#4 Argumente erleichtern eigenständiges Aufrufen, sonst nur über Funktion
if len(argv) == 4:
    skript, haltestelle, alinie, platzhalter = argv
    get01(haltestelle, alinie)
