# test.py
from webdriver_manager.chrome import ChromeDriverManager 
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService
import json
import time

driver = webdriver.Chrome()

webmotors = './data/search_links.json'


with open(webmotors, 'r') as file:
    data= json.load(file) 

links_das_motos=[]

for bike_list in data:
    
    moto = bike_list['moto']
    link = bike_list["link"]
    print(moto + " " + link)
    
    driver.get(link)
    driver.fullscreen_window()
    
    time.sleep(8)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    time.sleep(8)
    elements = driver.find_elements(By.CSS_SELECTOR, 'div.sc-bnXvFD.jKMjkg')
    
    for element in elements:
        link= element.find_element_by_css_selector("a")
        href= link.get_attribute('href')
        
        param=dict(nome_veiculo=moto, link_veiculo=href)
        links_das_motos.append(param)
        
        
    
    
    

# Add tests here


# primeiro pegar o link das motos
    #consegui encontrar elementos (supostamente)
    #vou iterar os elementos para achar os hrefs
    #colocar eles em um dicionário ou lista


# depois pegar link a link para ir pegando os elementos delas


