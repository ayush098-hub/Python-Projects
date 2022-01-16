
import csv
import requests

def getUrl():

    url=[]
    with open('urls.txt',newline='') as f:
     lines = csv.reader(f)
     for r in lines:
         url.append(r[0])
     return url

def getresponse():

 url=getUrl()

 try:
    for i in range(len(url)):
     actual_url='http://'+url[i]
     res= requests.get(actual_url,verify=True,timeout=5)
     print(url[i] ,"==",res.status_code,res.reason)
 except Exception as e:
        print(f'[ERROR]: {e}')

getresponse()

