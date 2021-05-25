import pandas as pd
import os
import time
from selenium import webdriver
import threading

def chrome_driver():
    driver = webdriver.Chrome()
    return driver

def kill_chrome():
    os.system("taskkill /f /im chrome.exe")
    os.system("taskkill /f /im chromedriver.exe")

def fetch_block(cities,thread__):
    path = r"C:\Users\user\Desktop\Neosoft\travello\city_data"  # The path where the data is stored
    thread__ = str(thread__)
    output_label_file = "image_data_uri_"+thread__+".csv"
    start_from = 0
    last_city = ""
    if os.path.exists(output_label_file):
        df = pd.read_csv(output_label_file)
        try:
            last_city = df.city.iat[-1]
            print(thread__+": Last city:", last_city)
        except: pass
        start_from = len(df)
    else:
        with open(output_label_file, 'w') as csv:
            csv.write("city,img1,img2,img3,img4\n")
    global total_count
    print(thread__+": Len of done citites:", start_from)
    
    cities = cities[start_from:]

    for row in cities.iterrows():
        #os.system("cls")
        total_count += 1
        print(thread__,":: Working on entry ", total_count)
        this_row = row[1]
        this_row = this_row.replace("city","")
        this_row = this_row.replace("country","")
        this_row = list(this_row)
        print(this_row)
        chrome = chrome_driver()
        print(thread__,":: Got driver")
        url1 = "https://www.google.com/search?q={city}+{country}+-map&hl=EN&tbm=isch".format(city=this_row[0], country=this_row[1])
        url2 = "https://www.google.com/search?q={city}+{country}+-map+streets&hl=EN&tbm=isch".format(city=this_row[0], country=this_row[1])
        chrome.get(url1)
        print(thread__,":: First url done")
        img = chrome.find_elements_by_xpath('//*[@class="rg_i Q4LuWd"]')
        img1 = img[0].get_attribute('src')
        img2 = img[1].get_attribute('src')
        chrome.get(url2)
        print(thread__,":: Second url done")
        img = chrome.find_elements_by_xpath('//*[@class="rg_i Q4LuWd"]')
        img3 = img[0].get_attribute('src')
        img4 = img[1].get_attribute('src')
        with open(output_label_file, 'a+') as csv:
                to_write = '"{}","{}","{}","{}","{}"\n'.format(this_row[0],img1,img2,img3,img4)
                csv.write(to_write)
        print(thread__,":: Written to csv")
        chrome.close()
        chrome.quit()
        print(thread__,":: Chrome Closed")
    
    
    

cities = pd.read_csv("city_data/cities.csv")
cities = cities[["city","country"]]

clear_counter = 0
total_count = 0

path = r"C:\Users\user\Desktop\Neosoft\travello\city_data"  # The path where the data is stored
output_label_file = "image_data_uri.csv"  # Output file path
files = os.listdir(path)

done_cities = []
last_city = ''
start_from = 0
if os.path.exists(output_label_file):
    df = pd.read_csv(output_label_file)
    try:
        last_city = df.city.iat[-1]
    except: pass
    start_from = len(df)
else:
    with open(output_label_file, 'w') as csv:
        csv.write("city,img1,img2,img3,img4\n")

print("Len of done citites:", start_from)
print("Last city:", last_city)
start_from += 5750
last_city_index = cities.loc[cities['city'] == last_city]
print(last_city_index)
total_count = start_from
print("Prev done till:",cities.loc[5750])

input()
cities = cities[start_from:]


cities_1 = cities[0:500]
cities_2 = cities[500:1000]
cities_3 = cities[1000:1500]
cities_4 = cities[1500:2000]
cities_5 = cities[2000:2500]
cities_6 = cities[2500:3000]
cities_7 = cities[3000:3500]
cities_8 = cities[3500:4000]
cities_9 = cities[4000:4500]
cities_10 = cities[4500:5000]

threads = list()
thread__1 = threading.Thread(target=fetch_block, args=(cities_1,11,))
thread__2 = threading.Thread(target=fetch_block, args=(cities_2,12,))
thread__3 = threading.Thread(target=fetch_block, args=(cities_3,13,))
thread__4 = threading.Thread(target=fetch_block, args=(cities_4,14,))
thread__5 = threading.Thread(target=fetch_block, args=(cities_5,15,))
thread__6 = threading.Thread(target=fetch_block, args=(cities_6,16,))
thread__7 = threading.Thread(target=fetch_block, args=(cities_7,17,))
thread__8 = threading.Thread(target=fetch_block, args=(cities_8,18,))
thread__9 = threading.Thread(target=fetch_block, args=(cities_9,19,))
thread__10 = threading.Thread(target=fetch_block, args=(cities_10,20,))

threads.append(thread__1)
threads.append(thread__2)
threads.append(thread__3)
threads.append(thread__4)
threads.append(thread__5)
threads.append(thread__6)
threads.append(thread__7)
threads.append(thread__8)
threads.append(thread__9)
threads.append(thread__10)

for th__ in threads:
    th__.start()

for th__ in threads:
    th__.join()











