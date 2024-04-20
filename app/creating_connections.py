from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import time

class HtMasterL:
    
    def __init__(self, path):
        self.path = path
        
    def connect_source(self, method):
        
        driver=webdriver.Chrome()
            
        driver.get(link)
        driver.fullscreen_window()
        
        time.sleep(8)
        
        content=driver.page_source
        soup= BeautifulSoup(content, 'html.parser')
        
        return soup
        
    
    