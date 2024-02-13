import pylightxl as xl
import times
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime

def parseDate(value):
    return datetime.strptime(value, "%Y/%m/%d").strftime("%d/%m/%Y")

driver = webdriver.Chrome()
driver.delete_all_cookies();
driver.maximize_window();   

db = xl.readxl('files/data.xlsx');
for index, row in enumerate(db.ws("datas").rows):
    if (index > 0):
        driver.get("https://treinamento.koden.com.br/Usuarios/Create")
        driver.find_element(By.ID, "NomeCompleto").send_keys(row[0])
        times.seconds(1)
        driver.find_element(By.ID, "EstadoCivil").send_keys(row[1])
        times.seconds(1)
        driver.find_element(By.ID, "DataNascimento").send_keys(parseDate(row[2]))
        times.seconds(1)
        driver.find_element(By.XPATH, '//*[@id="Sexo" and @value="' + row[3] + '"]').click()
        times.seconds(1)
        driver.find_element(By.XPATH, '//input[@type="submit" and @value="Create"]').click();        
        times.seconds(5)