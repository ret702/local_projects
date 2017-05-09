import requests
from bs4 import BeautifulSoup
import codecs
import re
import xml.etree.ElementTree as ET

def strip_non_ascii(string):
    ''' Returns the string without non ASCII characters'''
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped).rstrip()
urls=["http://www.filmsite.org/filmterms1.html","http://www.filmsite.org/filmterms2.html"
    , "http://www.filmsite.org/filmterms3.html","http://www.filmsite.org/filmterms4.html"
    , "http://www.filmsite.org/filmterms5.html","http://www.filmsite.org/filmterms6.html"
    , "http://www.filmsite.org/filmterms7.html","http://www.filmsite.org/filmterms8.html"
    , "http://www.filmsite.org/filmterms9.html","http://www.filmsite.org/filmterms10.html"
    , "http://www.filmsite.org/filmterms11.html","http://www.filmsite.org/filmterms12.html"
    , "http://www.filmsite.org/filmterms13.html","http://www.filmsite.org/filmterms14.html"
    , "http://www.filmsite.org/filmterms15.html","http://www.filmsite.org/filmterms16.html"
    , "http://www.filmsite.org/filmterms17.html","http://www.filmsite.org/filmterms18.html"
    , "http://www.filmsite.org/filmterms19.html","http://www.filmsite.org/filmterms20.html"]
root_xml_element = ET.Element("root")
for url in urls:
    page = requests.get(url)
    html=BeautifulSoup(page.content,'html.parser')
    table=html.find_all("table")
    count=0
    td_count=0
    title_desc_map={}
    last_element=""
    counter=0
    for t in table[2].find_all("tr"):
        if(count>3):
            table_data=t.find_all("td")
            print(table_data)
            if (len(table_data) >= 3):
                table_data[2].decompose()
            for x in table_data:
                temp=x.text.replace("\n","").replace("\r","")
                newstring = re.sub('\s+', ' ', temp)

                title_desc_map[td_count]=strip_non_ascii(newstring)
                if(title_desc_map[td_count]==''):
                    del title_desc_map[td_count]
                else:
                        if(counter==0):
                            last_element = title_desc_map[td_count]
                            child=ET.SubElement(root_xml_element,'title')
                            child.text=title_desc_map[td_count]
                            counter+=1
                        elif(counter==1):
                         child=ET.SubElement(root_xml_element,'description')
                         child.text=title_desc_map[td_count]
                         counter=0


                td_count+=1



        count+=1
#print(title_desc_map)
    tree=ET.ElementTree(root_xml_element)
    tree.write(r'C:\Users\Owner\Videos\data_to_xml.xml')
print(ET.tostring(root_xml_element))



