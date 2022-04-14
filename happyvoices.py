import requests
import random
from selenium import webdriver
import time
import pyperclip
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

from requests.structures import CaseInsensitiveDict

headers = CaseInsensitiveDict()
headers["authority"] = "etherscan.io"
headers["accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
headers["accept-language"] = "en-US,en;q=0.9"
headers["cache-control"] = "max-age=0"
headers["cookie"] = "ASP.NET_SessionId=eiyxz2vx1bm3syeufmwqmqkb; __cflb=02DiuFnsSsHWYH8WqVXcJWaecAw5gpnmeCUrEsE4kGwwA; __cf_bm=rhs_IFC5.2_MNlfUScpe6OAvEaI78VJD8LmeKoA9ygI-1649838489-0-AdueZ0IMjqjR6vz713c/hliseSR5R9HPl4UdhgugV8CHincbAGxycpUYjMWb3KCC0F67xhfdeqACi3NG2fSRqFI4TJwDNYG7qm4jNRbhjwTkMqWj2SCNvezmaVNeaevhZQ=="
headers["sec-ch-ua"] = 'Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"'
headers["sec-ch-ua-mobile"] = "?0"
headers["sec-ch-ua-platform"] ='"Windows"'
headers["sec-fetch-dest"] = "document"
headers["sec-fetch-mode"] = "navigate"
headers["sec-fetch-site"] = "none"
headers["sec-fetch-user"] = "?1"
headers["upgrade-insecure-requests"] = "1"
headers["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"

driver = webdriver.Chrome(executable_path = 'C:\\Users\\Carter\\Desktop\\flights\\chromedriver')
final_results = set()
with open("happyvoicesTokens.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        v = line.strip().split(",")
        item = v[0]
        name = v[1]

        url = "https://etherscan.io/token/0x495f947276749ce646f68ac8c248420045cb7b5e?a=" + item + "#inventory"
        
        


        driver.get(url)
        time.sleep(7)
        driver.switch_to.frame('tokenerc721_inventory_pageiframe')


        stringoftext = driver.find_element_by_xpath('//*[@id="body"]/div[1]/p').text
        unique_tokens = int(stringoftext.split(" ")[3])
        
        if unique_tokens <= 0:
            print("No unique tokens found for: " + name)
            continue
        holders = []
        #print("Holders for: " + name)
        for i in range(1, unique_tokens + 1):
            v = driver.find_element_by_xpath('//*[@id="grid-container"]/div[' + str(i) + ']/div/div[2]/a')
            
            #print(v.text)
            final_results.add(v.text)
        time.sleep(2)

for address in sorted(final_results):
    print(address)