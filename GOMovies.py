
# coding: utf-8

# In[ ]:

import requests
from bs4 import BeautifulSoup
import time

library = ['0-9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

text_file = open("Output1.csv", "w")


with open("Output1.csv", "w") as text_file:
    st = "index,title,quality,genere,imdb"
    print(st)
    print(st, file=text_file)
    index=0
    
    for i in range(len(library)):
        nxtlink = "https://gostream.is/movies/library/"+library[i]
        page = requests.get(nxtlink)
        soup = BeautifulSoup(page.content, 'xml')
        time.sleep(1)
        
        num=1
        maxs=0
        pagenum=1
        
        for link in soup.findAll('div', attrs ={"id":"main"}):
            for link in soup.findAll('table', attrs ={"class":"table table-striped"}):
                for link in soup.findAll('tr', attrs ={"class":"mlnew-head"}):
                    maxs = int(link.find_next('td',attrs ={"class":"mlnh-letter"}).getText().replace('results','').replace(' ','').replace('#',''))
        
        while (num<maxs):
            time.sleep(1)
            nxtlink = "https://gostream.is/movies/library/"+library[i]+"/"+str(pagenum)
            page = requests.get(nxtlink)
            soup = BeautifulSoup(page.content, 'xml')
            pagenum=pagenum+1
            for link in soup.findAll('div', attrs ={"id":"main"}):
                for link in soup.findAll('table', attrs ={"class":"table table-striped"}):
                    count=1;
                    for link in soup.findAll('tr',attrs={"class":"mlnew"}):
                        num=num+1
                        index=index+1
                        title = link.find_next('td',attrs ={"class":"mlnh-2"}).getText().replace('\n','').replace(',',' ')
                        quality = link.find_next('td',attrs ={"class":"mlnh-3"}).getText().replace('\n','').replace(' ','').replace(',','|')
                        genere = link.find_next('td',attrs ={"class":"mlnh-5"}).getText().replace('\n','').replace(' ','').replace(',','|')
                        imdb = link.find_next('td',attrs ={"class":"mlnh-6"}).getText().replace('\n','').replace(' ','').replace(',','|')
                        st = str(index)+","+title+","+quality+","+genere+","+imdb
                        print(st)
                                         
        
    
   


# In[ ]:



