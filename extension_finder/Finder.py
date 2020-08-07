"""
Finder.py -
@brad_anton

Simple Script to identify which browser extensions are installed on a system. 

"""
import platform
import re
import os
import sys,time
import csv
import datetime
from tabulate import tabulate
from Constants import MacBrowsers, WinBrowsers
from Browsers.Chrome import Chrome
from Browsers.InternetExplorer import InternetExplorer
from Browsers.Firefox import Firefox


class Finder:
    def __init__(self, directory=None):
        operating_system = platform.system()
        
        self.os = None
        
        if operating_system == 'Darwin':
            self.os = MacBrowsers
        elif operating_system == 'Windows':
            self.os = WinBrowsers
        else:
            print "[!] Unsupported Operating System!!"
            return
        
    def print_extensions(self):
        today_string = datetime.datetime.today().strftime('%x')
        c = Chrome(self.os)
        print ("Chrome")
        print tabulate(c.extensions(), headers="keys", tablefmt="tsv")
        content_c = tabulate(c.extensions(), headers="keys", tablefmt="tsv")
        content2_c = content_c.replace('\t', ',')

        text_file=open("output\Chrome.csv","w")
        text_file.write(content2_c)
        text_file.close()

        if self.os == WinBrowsers: 
            i = InternetExplorer(self.os)
            print ("IE")
            print tabulate(i.extensions(), headers="keys")
  
            content1 = tabulate(i.extensions(), headers="keys", tablefmt="tsv")
            content2 = content1.replace('\t', ',')
            
            text_file=open("output\IE.csv","w")
            text_file.write(content2)
            text_file.close()

            #path = os.getenv('APPDATA') + '\Mozilla\Firefox\Profiles\ijfnxm93.default-release\extensions'
            path = os.getenv('APPDATA') + '\Mozilla\Firefox\Profiles\vv1evrak.default\extensions'

            files = []
    
            for r, d, f in os.walk(path):
                for file in f:              
                    files.append((file))


            table = [] 
            print ("Firefox")
            print ("extension" + "\t\t\t" + "date_created")
            print ("----------------------------------------------")
            for f in files:
                print (f) + "\t\t\t" + (time.ctime(os.path.getctime(path + "\\" + f)))
                #print (f),time.ctime('%a, %b %d,%Y %I:%M:%S',time.ctime(os.path.getctime(path + "\\" + f)))
            
            with open('output\Firefox.csv','wb') as file:
                file.write("file" + ",")
                file.write("date_created")
                file.write('\n')
                for line in files:
                    file.write(line + ",")
                    file.write(time.ctime(os.path.getctime(path + "\\" + f)))
                    file.write('\n')


        
if __name__ == '__main__':
    f = Finder()
    f.print_extensions()

