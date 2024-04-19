# test.py
from webdriver_manager.chrome import ChromeDriverManager 
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService
import json
import time

driver = webdriver.Chrome()

webmotors_path = './data/search_links.json'
individual_links_path = './data/individual_links.json'


with open(webmotors_path, 'r') as file:
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
        
        with open('data')
        
        
# função para abrir um link e expandir ele
    # e no final retornar o html da página completo
    
#função para extrair os hrefs do html
    # e retornar um arquivo json desses links
    
#função para extrair os elementos de cada do json de links
    # e retornar outro arquivo com todas as infos para ficar salvo
    
    
    
