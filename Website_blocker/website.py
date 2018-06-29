##This Program is used to block unwanted websites at specific times

# Importing all needed Libraries
import time
from datetime import datetime as dt

# Path of hosts file
hosts_path = r'C:\Windows\System32\drivers\etc\hosts'

hosts_temp = 'hosts'

#The Ip Address 
redirect = '127.0.0.1'

website_list = ['www.filgoal.com ' , 'www.yallakora.com ']


while True:
    if dt(dt.now().year,dt.now().month , dt.now().day ,12) < dt.now() <dt(dt.now().year,dt.now().month , dt.now().day ,16):
        print('working hours .....')
        with open(hosts_path , 'r+' ) as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+' '+website+'\n')
    else:
        print('fun hours ... ')
        with open(hosts_path , 'r+' ) as file:
            content = file.readLines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
            
        
    time.sleep(5)
