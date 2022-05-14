from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import requests
from bs4 import BeautifulSoup
import time
import re
import random

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os

url = 'https://www.coupang.com/'
options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
userAgent="user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
options.add_argument(userAgent)

browser = webdriver.Chrome(executable_path='/Users/chromedriver',chrome_options=options)
browser.maximize_window()
browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", { "source": """ Object.defineProperty(navigator, 'webdriver', { get: () => undefined }) """ })
browser.get(url)
time.sleep(random.uniform(1,3))

# #스크롤내림
prev_height = browser.execute_script("return document.body.scrollHeight")
while True:
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(random.uniform(1,3))
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if prev_height == curr_height:
        break
    prev_height = curr_height
    
    
time.sleep(random.uniform(1,3))



page_url = browser.page_source
soup = BeautifulSoup(page_url,"lxml")

box =soup.find("div",{"id":"categoryBestUnit"})
titles=box.find_all('a',{"class":'category-best-link'})
title = 'https://www.coupang.com'+titles[1]['href']
print(title)