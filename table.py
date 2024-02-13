from selenium import webdriver
from selenium.webdriver.common.by import By
import times

driver = webdriver.Chrome()
driver.delete_all_cookies();
driver.maximize_window();    
driver.get("https://treinamento.koden.com.br/Usuarios")
table = driver.find_element(By.ID, "tabelaUsuarios")
for index, row in enumerate(table.find_elements(By.TAG_NAME, "tr")):
    if (index > 0):
        for td in row.find_elements(By.TAG_NAME, "td"):
            print (td.text)