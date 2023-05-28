# importamos las librerias de selenium
import re
from selenium import webdriver
from selenium.webdriver.common.by import By

def get_all_links(driver):
    links = set()
    for a in driver.find_elements(By.TAG_NAME, 'a'):
        link = a.get_attribute('href')
        if link:
            links.add(link)
    return links

def count_occurrences(string, substring):

    pattern= r"\bURJC\b"
    matches = re.findall(pattern, string)
    return len(matches)

##### MAIN PROGRAM ####
driver = webdriver.Chrome()
visited_links = set()
all_links = set()
# Visitar la página principal
driver.get('https://r2-ctf-vulnerable.numa.host/')
# Obtener todos los enlaces de la página principal
all_links = get_all_links(driver)

# Recorrer recursivamente todos los enlaces de la página principal y sus enlaces hijos
while all_links:
    link = all_links.pop()
    if link.startswith('https://r2-ctf-vulnerable.numa.host/') and link not in visited_links and not link.endswith('#'):
        visited_links.add(link)
        driver.get(link)
        print(f"Visitando: {link}")
        child_links = get_all_links(driver)
        for child_link in child_links:
            if child_link.startswith('https://r2-ctf-vulnerable.numa.host/') and child_link not in visited_links and not child_link.endswith('#'):
                all_links.add(child_link)

# Contar las apariciones de "URJC" en todas las páginas visitadas
count = 0
for link in visited_links:
    driver.get(link)
    page_source = driver.page_source
    count += count_occurrences(page_source, 'URJC')
print(f"El número de apariciones de 'URJC' en todas las páginas visitadas es: {count}")

# Cerrar el navegador
driver.quit()


