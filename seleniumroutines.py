from selenium import webdriver
from selenium.webdriver.common.by import By
import times

def seleniumRoutines():    
    driver = webdriver.Chrome()
    driver.delete_all_cookies();
    driver.maximize_window();    
    driver.get("https://treinamento.koden.com.br/Usuarios/Create")
    driver.find_element(By.ID, "NomeCompleto").send_keys("Souza e Test")
    times.seconds(1)
    driver.find_element(By.ID, "EstadoCivil").send_keys("Solteiro")
    driver.find_element(By.ID, "DataNascimento").send_keys("10/01/2005")
    driver.find_element(By.XPATH, '//*[@id="Sexo" and @value="Masculino"]').click()
    driver.find_element(By.XPATH, '//input[@type="submit" and @value="Create"]').click();
    times.seconds(15)