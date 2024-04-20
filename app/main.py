# test.py
from webdriver_manager.chrome import ChromeDriverManager 
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService
import json
import time

webmotors_path = './data/search_links.json'
individual_links_path = './data/individual_links.json'


with open(webmotors_path, 'r') as file:
    data= json.load(file) 

links_das_motos=[]

for bike_list in data:
    print('oi')
