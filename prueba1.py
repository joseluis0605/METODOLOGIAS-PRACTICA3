'''
selenium se usa para automatizar busquedas y acciones en una pagina web
por ejemplo, que pulse algun elemento, que busque, que escriba en algun lado

web driver: interfaz que nos permite simular la conexion de un usuario con un buscador
para ello nos descargamos el web driver de chrome y tendremos en cuenta la ruta para mas
adelante
web driver wait: se usa para darle tiempo al html para que se cargue cuando nos metemos en una pagina
expected_condition: se usa para tratar la condicion esperada



'''

# importamos las librerias de selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# driver es donde se va a cargar el explorador que usemos, en nuestro caso Google Chrome
driver= webdriver.Chrome("C:\\Users\\USUARIO\\Desktop\\selenium\\chromedriver.exe")

# llamamos con nuestro driver a una direccion, es decir, nos metemos en la direccion indicada
driver.get("https://gmail.com")

# cerramos el buscador
driver.close()


