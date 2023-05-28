# importamos las librerias de selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver= webdriver.Chrome()
driver.get("C:\\Users\\USUARIO\\Desktop\\URJC\\3º Ciberseguridad\\2º CUATRIMESTRE\\METODOLOGIA  DESARROLLO SEGURO\\PRACTICA 3\\TOPOS\\index.html")
contador= 0
time.sleep(5)
while contador < 10000:
    hole = driver.find_elements(By.CLASS_NAME, "hole")
    hole[0].click()
    hole[1].click()
    hole[2].click()
    hole[3].click()
    hole[4].click()
    hole[5].click()
    hole[6].click()
    hole[7].click()
    hole[8].click()
    hole[9].click()
    hole[10].click()
    hole[11].click()
    hole[12].click()
    hole[13].click()
    hole[14].click()
    hole[15].click()

    actual= driver.find_element(By.ID, 'score')
    contador=int(actual.text)
input()
driver.close()

'''
    for i in range(16):
        hole[i].click()
'''