import pandas as pd
from requests import get 
from bs4 import BeautifulSoup
ma_page=pd.read_html("http://fr.wikipedia.org/wiki/Liste_des_champions_de_tennis_vainqueurs_en_Grand_Chelem_en_simple",header="infer")
url= 'https://www.stat4decision.com/fr/packages-python-data-science/'
reponse = get(url)
print(reponse.text[:50])
html_soup=BeautifulSoup(reponse.text,'html.parser')
noms_packages=html_soup.find_all('div',class_='x-accordion-heading')
for div_nom in noms_packages:
    print(div_nom.text.split(",")[0].capitalize())
tableaux_records=ma_page[24]
tableaux_records.head()