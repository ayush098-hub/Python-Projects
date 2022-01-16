import requests

def getUrl():
 url = []
 i=0
 n=int(input("Enter number of websites:"))
 while i<n:
    try:
        line = input("Enter Website Address:")
    except EOFError:
        break
    url.append('http://'+line)
    i+=1

 url = list(map(str, url)) 
 return url

def getresponse():

 url=getUrl()

 try:
    for i in range(len(url)):
     actual_url=url[i]
     res= requests.get(actual_url,verify=True,timeout=5)
     print("Status code of",url[i] ,"is",res.status_code,res.reason)
 except Exception as e:
        print(f'[ERROR]: {e}')

getresponse()
