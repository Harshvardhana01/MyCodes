print('''
Hey How are you today
What can i get you this time''')
import os,glob,random,webbrowser
from datetime import datetime as dt
helloIntent = ["hi","hello","hey","wassup","hey buddy"]
dateIntent = ["date","show me date","date please","whats the date"]
timeIntent = ["time","show me time","time please","whats the time"]
newsIntent = ["news","show me news","news today","News on fox"]
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

elif msg in newsIntent:
    import urllib.request as url
    import bs4

    #Newssearch = input("Find News about:")
    print('''
    Press 1 for Entertainment
    Press 2 for politics
    Press 3 for media
    Press 4 for business
    press 4 for sports''')
    newssearch = int(input("Enter your choice:"))

    path = "https://www.foxnews.com/"
    response = url.urlopen(path)

    if newssearch == 1:
        path = path+'entertainment'
        response = url.urlopen(path)
        data = bs4.BeautifulSoup(response,'lxml')
        h4List = data.findAll('h4',class_='title')
        h4List = h4List[0:10]

        for i in range(len(h4List)):
            print(f'{i+1}--{h4List[i].text}/n')

    elif newssearch == 2:
        path = path+'politics'
        response = url.urlopen(path)
        data = bs4.BeautifulSoup(response,'lxml')
        h4List = data.findAll('h4',class_='title')
        h4List = h4List[0:10]

        for i in range(len(h4List)):
            print(f'{i+1}--{h4List[i].text}/n')
    elif newssearch == 3:
        path = path+'media'
        response = url.urlopen(path)
        data = bs4.BeautifulSoup(response,'lxml')
        h4List = data.findAll('h4',class_='title')
        h4List = h4List[0:10]

        for i in range(len(h4List)):
            print(f'{i+1}--{h4List[i].text}/n')

    elif newssearch == 4:
        path = path+'business'
        response = url.urlopen(path)
        data = bs4.BeautifulSoup(response,'lxml')
        h4List = data.findAll('h3',class_='title')
        h4List = h4List[0:10]

        for i in range(len(h4List)):
            print(f'{i+1}--{h4List[i].text}/n')
    elif newssearch == 5:
        path = path+'sports'
        response = url.urlopen(path)
        data = bs4.BeautifulSoup(response,'lxml')
        h4List = data.findAll('h3',class_='title')
        h4List = h4List[0:10]

        for i in range(len(h4List)):
            print(f'{i+1}--{h4List[i].text}/n')

else:
    print('Sorry.....Cant understand you properly')




    
