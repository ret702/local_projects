import requests
from bs4 import BeautifulSoup
import codecs
import re

def strip_non_ascii(string):
    ''' Returns the string without non ASCII characters'''
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped).rstrip()

page = requests.get("http://www.filmsite.org/filmterms1.html")
html=BeautifulSoup(page.content,'html.parser')
table=html.find_all("table")
file=codecs.open(r'C:\Users\Owner\Videos\scraped_data.txt','wb', 'utf8')
count=0
td_count=0
title_desc_map={}
for t in table[2].find_all("tr"):
    if(count>3):
        table_data=t.find_all("td")
        if (len(table_data) == 3):
            table_data[2].decompose()
        for x in table_data:
            temp=x.text.replace("\n","").replace("\r","")
            newstring = re.sub('\s+', ' ', temp)
            title_desc_map[td_count]=strip_non_ascii(newstring)
            file.write(title_desc_map[td_count] + "\n")
            td_count+=1



    count+=1
print(title_desc_map)

file.close()


