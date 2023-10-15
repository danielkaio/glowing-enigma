from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import openpyxl


servico = Service(ChromeDriverManager().install())

internet = webdriver.Chrome(service=servico)

 

internet.get("https://www.uol.com.br/")

noticias = internet.find_elements(By.XPATH,"//h3[@class='title__element headlineSub__content__title']")

for noticia in noticias:
    print(noticia.text)
    
    
    
planilha = openpyxl.Workbook()
planilha_pagina  = planilha.create_sheet('noticias')
nc = planilha['noticias']
nc['A1'].value='noticias'



for noticia in noticias:
    nc.append([noticia.text])
planilha.save('noticias.ods')

  
  
    
    



  




