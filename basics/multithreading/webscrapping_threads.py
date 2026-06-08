import threading
import time 
import requests
from bs4 import BeautifulSoup

urls=[
    'https://en.wikipedia.org/wiki/Elon_Musk',
    'https://en.wikipedia.org/wiki/Jeff_Bezos',
    'https://en.wikipedia.org/wiki/Albert_Einstein'
]

def get_content(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.content,'html.parser')
    print(soup.text)


if __name__=='__main__':
    threads=[]
    for url in urls:
        thread=threading.Thread(target=get_content,args=(url,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    print('All web pages fetched')