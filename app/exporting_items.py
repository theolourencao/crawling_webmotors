from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import requests
import time

link ="https://www.webmotors.com.br/comprar/honda/pcx/151cc/2018/2211593?pos=a2211593g:&np=1"



def exporting_vehicle_data(link):
    """This function extracts all valuable information from each announced vehicle link

    Args:
        link (_type_): The link of each available vehicle
    """

    driver=webdriver.Chrome()
    
    driver.get(link)
    driver.fullscreen_window()
    
    time.sleep(8)
    
    content=driver.page_source
    soup= BeautifulSoup(content, 'html.parser')

    vehicle_data = {}

    location_element = soup.find('strong', {'id': 'VehiclePrincipalInformationLocation'})
    
    
    if location_element:
        vehicle_data['localizacao'] = location_element.text.strip()
        
        
    else:
        vehicle_data['localizacao']= None
    
    return vehicle_data
    

print(exporting_vehicle_data(link))