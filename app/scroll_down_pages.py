from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService
import time
from bs4 import BeautifulSoup

link="https://www.webmotors.com.br/motos/sp-sao-paulo/yamaha/nmax-160-abs?estadocidade=S%C3%A3o%20Paulo%20-%20S%C3%A3o%20Paulo&tipoveiculo=motos&localizacao=-23.5505199,-46.6333094x0km&marca1=YAMAHA&modelo1=NMAX%20160%20ABS&lkid=1039"

def scroll_down_pages(link):
    """It goes through the links and scrolls down the pages 
    in order to save complete htmls as variables

    Args:
        link (_type_): The link that is made from the list of links
    """
    driver = webdriver.Chrome()
    # test.py
    
    driver.get(link)
    driver.fullscreen_window()
    
    time.sleep(8)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(8)
    
    content= driver.page_source
    soup= BeautifulSoup(content,'html.parser')
    return soup
    
print(scroll_down_pages(link))
    