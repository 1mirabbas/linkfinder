#!/usr/bin/env python3
# Version: v1.0.0 @2023

###########################################
#    Author: Mirabbas Aghalarov           #
#    Youtube: mirabbasaghalarov           #
#    Instagram: 1mirabbas                 #
#    Linkedin: mirabbasagalarov           #
#    Email: mirabbasagalarov0@gmail.com   #
###########################################


import argparse
import requests
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument("-u", help="target url", dest='url')
parser.add_argument("-o", help="output file", dest='output')



args = parser.parse_args()
output = args.output
url = args.url


def prRed(skk):print("\033[91m{}\033[00m".format(skk))
def prCyan(skk):print("\033[96m{}\033[00m".format(skk))
def prGreen(skk):print("\033[92m{}\033[00m".format(skk))
def prMagenta(skk):print("\033[35m{}\033[00m".format(skk))
def prBlue(skk):print("\033[34m{}\033[00m".format(skk))


prCyan('''
 _     _       _  __ __ _           _           
| |   (_)_ __ | |/ // _(_)_ __   __| | ___ _ __ 
| |   | | '_ \| ' /| |_| | '_ \ / _` |/ _ \ '__|
| |___| | | | | . \|  _| | | | | (_| |  __/ |   
|_____|_|_| |_|_|\_\_| |_|_| |_|\__,_|\___|_|   
        Author: Mirabbas Aghalarov                                  
''')

prGreen('''
1)<script>
2)<link>
3)<a>
4)all
''')

try:
    value = input('Please select the mode: ')
    value=int(value)
except ValueError:
    prRed('Error')

if url is None:
    prRed("""Missing target! ==>","Usage: linkfinder.py -u https://example.com""")
    print("")
else:
    if output is None:
        if value ==1:
            page=requests.get(url)
            soup= BeautifulSoup(page.text,'html.parser')
            aaa=soup.find_all('script')
            for i in aaa:
                a=i.get('src')
                if a== None:
                    pass
                else:
                    print(a)
        elif value ==2:
            page=requests.get(url)
            soup= BeautifulSoup(page.text,'html.parser')
            aaa=soup.find_all('link')
            for i in aaa:
                a=i.get('href')
                if a== None:
                    pass
                else:
                    print(a)
        elif value ==3:
            page=requests.get(url)
            soup= BeautifulSoup(page.text,'html.parser')
            aaa=soup.find_all('a')
            for i in aaa:
                a=i.get('href')
                if a== None:
                    pass
                else:
                    print(a)

        elif value ==4:
            page=requests.get(url)
            soup= BeautifulSoup(page.text,'html.parser')
            aaa=soup.find_all('link')
            bbb=soup.find_all('script')
            ccc=soup.find_all('a')
            for i in aaa:
                a=i.get('href')
                if a== None:
                    pass
                else:
                    print(a)
            for i in bbb:
                b=i.get('src')
                if b== None:
                    pass
                else:
                    print(b)
            for i in ccc:
                c=i.get('href')
                if c== None:
                    pass
                else:
                    print(c)

        else:
            prRed('''Please choose the mode properly''')
    else:
        with open(output, "a") as f:
            if value ==1:
                page=requests.get(url)
                soup= BeautifulSoup(page.text,'html.parser')
                aaa=soup.find_all('script')
                for i in aaa:
                    a=i.get('src')
                    if a== None:
                        pass
                    else:
                        f.write(a+'\n')
            elif value ==2:
                page=requests.get(url)
                soup= BeautifulSoup(page.text,'html.parser')
                aaa=soup.find_all('link')
                for i in aaa:
                    a=i.get('href')
                    if a== None:
                        pass
                    else:
                        f.write(a+'\n')
            elif value ==3:
                page=requests.get(url)
                soup= BeautifulSoup(page.text,'html.parser')
                aaa=soup.find_all('a')
                for i in aaa:
                    a=i.get('href')
                    if a== None:
                        pass
                    else:
                        f.write(a+'\n')

            elif value ==4:
                page=requests.get(url)
                soup= BeautifulSoup(page.text,'html.parser')
                aaa=soup.find_all('link')
                bbb=soup.find_all('script')
                ccc=soup.find_all('a')
                for i in aaa:
                    a=i.get('href')
                    if a== None:
                        pass
                    else:
                        f.write(a+'\n')
                for i in bbb:
                    b=i.get('src')
                    if b== None:
                        pass
                    else:
                        f.write(b+'\n')
                for i in ccc:
                    c=i.get('href')
                    if c== None:
                        pass
                    else:
                        f.write(c+'\n')
            else:
                prRed('''Please choose the mode properly''')








