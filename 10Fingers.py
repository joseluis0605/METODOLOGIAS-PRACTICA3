# importamos las librerias de selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver= webdriver.Chrome()
driver.get("C:\\Users\\USUARIO\\Desktop\\URJC\\3º Ciberseguridad\\2º CUATRIMESTRE\\METODOLOGIA  DESARROLLO SEGURO\\PRACTICA 3\\FINGERS\\index.html")
wait = WebDriverWait(driver, 10)
#localizamos la primera palabra
elemento = driver.find_element(By.CLASS_NAME, "current")
# localizamos le recuadro
recuadro = driver.find_element(By.ID, "textInput")

for i in range (20):
    # sacamos la primera palabra
    word = elemento.text

    # metemos la palabra
    recuadro.send_keys(word)
    recuadro.send_keys(Keys.SPACE)
    #nos colocamos sobre la nueva palabra
    elemento = driver.find_element(By.CLASS_NAME, "current")


input()
driver.close()