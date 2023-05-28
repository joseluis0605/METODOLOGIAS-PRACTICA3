# importamos las librerias de selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# iniciamos el driver
driver= webdriver.Chrome()
# nos metemos en la pagina
driver.get("https://gmail.com")

# para hacer click podemos usar muchos tipos de identificadores, class, id, css, xpath...
boton = driver.find_element(By.CSS_SELECTOR, 'button#id-del-boton') # encontramos el elemento
boton.click() # realizamos busqueda

#para meter una palabra en un texto
palabra= driver.find_element(By.CLASS_NAME, "input#id-del-cuadro-de-texto")
palabra.send_keys("palabra")

# para extraer una palabra del texto
elemento = driver.find_element(By.ID, 'selector-del-elemento')
palabra = elemento.text
print(palabra)

input()
# cerramos el buscador
driver.close()
