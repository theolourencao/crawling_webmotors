from bs4 import BeautifulSoup
import re 
import pandas as pd
from creating_connections import HtMasterL

path= '../data/html_exemplo.html'

def get_links(modelo,path):
    
    """
    Com essa função você terá um dataframe de todos os links da página que você acessou

    Returns:
        df
    """
    
    link_list=[]
    
    ht= HtMasterL(path)
    
    soup = ht.connect_source("FILE", False)
    
    
    for link in soup.find_all('a', attrs={'href': re.compile("^https://")}):
        link_list.append(link.get('href'))
        
    df= pd.DataFrame(link_list,columns=['link']).drop_duplicates()
    df['modelo'] = modelo
    return df
    


print(get_links("NMAX",path))