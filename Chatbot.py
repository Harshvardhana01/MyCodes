
Introform = ["Hi","Hello","Wasaap","Hey","Hola"]
Status = ["Good","Nice","Better","I am Fine","Not Good","Sad","Dipressed"]


Introform = str(input("Enter msg:")).lower
    
if Introform:
    print("Hello.....How are you ?")

else:
    print("Cant understand your properly")


Status = str(input("Good / Not so good")).lower

if Status:
    print("Greatings for your  better future")

else:
    print("Cant understand you")


import os,glob,random,webbrowser
from datetime import datetime as dt
helloIntent = ["hi","hello","hey","wassup","hey buddy"]
dateIntent = ["date","show me date","date please","whats the date"]
timeIntent = ["time","show me time","time please","whats the time"]
msg = input("Enter Message : ")
msg = msg.lower()
musicIntent = ["music","play music"]

if msg in helloIntent:
    print("hello Sir....")
elif msg in dateIntent:
    datetime = dt.now()
    date = datetime.strftime("%d-%m-%y,%a")
    print(date)
elif msg in timeIntent:
    datetime = dt.now()
    time = datetime.strftime("%I:%M:%S,%p")
    print(time)
elif msg in musicIntent:
    os.chdir(r"")#raw string
    #list=os.listdir()
    song = glob.glob("*.mp3")
    os.startfile(random.choice(song))
elif msg.startswith("open"):
    name=msg.split()[-1]+".com"
    webbrowser.open(name)




    
