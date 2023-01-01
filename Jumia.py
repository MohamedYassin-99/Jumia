# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 14:45:55 2022

@author: hamoy
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
Lap_Products =  []
for i in range(1,11):     ##Lop for the number of pages which will scraped
    Url = f"https://www.jumia.com.eg/acer--asus--dell--gigahertz--hp--lenovo--samsung/?q=laptop&shipped_from=country_local&page={i}#catalog-listing"
    response = requests.get(Url)
    response = response.content
    soup = BeautifulSoup(response, 'html.parser')
    All_Products= soup.findAll('article',class_='prd _fb col c-prd')
   
    for p in All_Products:
        Product =p.find('h3',class_='name').text
        price = p.find('div', class_='prc').text
        discount= getattr(p.find('div', class_='bdg _dsct _sm'),'text',0)  ##Replace the none to be text then replace by zero
        Image= p.find('img')
        Lap_Products.append([Product,price,discount,Image['data-src']])
   
    
df = pd.DataFrame(Lap_Products,columns=["Product","Price","Discount","Image"])
df.to_csv('Laptop.csv')
 



