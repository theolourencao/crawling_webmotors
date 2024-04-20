from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import time

class HtMasterL:
    
    """In order to connect your files i created this class
    """
    
    def __init__(self, path):
        self.path = path
        
    def connect_source(path, method, scrolldown: bool):
        
        if method=="WEB":
        
            driver=webdriver.Chrome()
                
            driver.get(path)
            
            if scrolldown==True:
                driver.fullscreen_window()
                
            
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            
            time.sleep(8)
            
            content=driver.page_source
        
        elif method=="FILE":
            
            with open(path, 'r') as file:
                content=file.read()
            
            
    

        soup= BeautifulSoup(content, 'html.parser')
        
        return soup
        
    
    