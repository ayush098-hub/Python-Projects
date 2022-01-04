
#--------------------------------------------------------------Header Modules--------------------------------------------------------------
from pyfiglet import Figlet
from termcolor import colored, cprint

#--------------------------------------------------------------Main Modules--------------------------------------------------------------
import sys
import requests
from bs4 import BeautifulSoup


#--------------------------------------------------------------Header Part-------------------------------------------------------------- 
custom_fig = Figlet(font='standard')
print(colored('===================================================================','blue'))
print(colored(custom_fig.renderText('BOOK  FINDER !'),'green'))
print(colored('===================================================================','blue'))
print_red=lambda x:cprint(x,'yellow')
print_red("Created By: Ayush Verma, Date:27-08-2021")
print_red("Follow me on instagram: @_3xabyt3_")
print()

#--------------------------------------------------------------Functioning Part--------------------------------------------------------------
book_name=input("Please enter the book name: ")

while True:
 
 try:
     page_no=int(input("Enter the page number on which you want to search for ex- 1:"))

 except ValueError:
    print('\nPlease enter integer value !')
    sys.exit(0)
 

 url='https://1lib.in/s/'+book_name+'?page='+str(page_no)
 page = requests.get(url)

 soup = BeautifulSoup(page.content,"html.parser")

 results = soup.find(id="searchResultBox")

 book_elements = results.find_all("div", class_="resItemBox resItemBoxBooks exactMatch")


 for book_element in book_elements:
    
    title_element = book_element.find("h3", itemprop="name")


    print("Title: ",title_element.text.strip())

    
    for h in book_element.find_all('h3', itemprop="name"):
        a = h.find('a')
        Book_Link="https://1lib.in"+a.attrs['href']
        dl_link=str(Book_Link.replace('book','dl'))
        print("Book Description:",Book_Link)
        print("Download Link",dl_link)
        print()
 
 print("If you got your book, please enter q to quit or enter c to continue:") 
 print("If you see no any links, it means there is no any matching book for you !")
 terminate=input("Enter your choice:")
 if terminate=='q':     
     break
 elif terminate=='c':
     continue

