import requests
import json

mass = []
with open("list.txt") as f:
    for line in f:
        mass.append([str(x) for x in line.split()])
myFile = open('out.txt','a')
with myFile:
    for i in range(len(mass)):
        try:
            api_param = {
                "inn": mass[i],
                "key":"607h3hCQhyqeAPNp"
                }
            res = requests.get(
                f"https://api.checko.ru/v2/finances",
                params=api_param)
            myFile.write(str(api_param ["inn"]) + " " + str((res.json()["data"]["2021"]["2110"])) +'\n')
            #print (str(api_param ["inn"]) + " " + str((res.json()["data"]["2021"]["2110"])))
        except:
            myFile.write(str(api_param ["inn"]) + " " +"Нет данных"+'\n')
             #print (str(api_param ["inn"]) + " Нет данных")
    
