from bs4 import BeautifulSoup
import re 
import pandas as pd

html_path= '../data/html_exemplo.html'


with open(html_path, 'r') as file:
    file_site=file.read()

def get_links(modelo,file_site):
    
    """
    Com essa função você terá um dataframe de todos os links da página que você acessou

    Returns:
        df
    """
    
    link_list=[]
    
    soup= BeautifulSoup(file_site, 'html.parser')
    for link in soup.find_all('a', attrs={'href': re.compile("^https://")}):
        link_list.append(link.get('href'))
        
    df= pd.DataFrame(link_list,columns=['link']).drop_duplicates()
    df['modelo']= modelo
    return df
    


print(get_links("NMAX",file_site))