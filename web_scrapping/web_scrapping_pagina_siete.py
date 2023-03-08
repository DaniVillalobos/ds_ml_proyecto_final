import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")
driver = webdriver.Chrome(options=options)

# Navegar a la página principal
url = "https://www.paginasiete.bo/economia"
driver.get(url)

boton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, '_1030065096_myMoreButton')))
driver.execute_script("arguments[0].scrollIntoView();", boton)

l=0
# ... realizar cualquier acción que desee con el elemento
for i in range(400): # Voy a darle click en cargar la cantidad de veces
        time.sleep(3)
        boton.click()
        # Esperar 2 segundos para que se cargue la página
        time.sleep(3)
        # busco el boton nuevamente para darle click en la siguiente iteracion
        boton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, '_1030065096_myMoreButton')))
        driver.execute_script("arguments[0].scrollIntoView();", boton)
        l=l+1
        print(l)
# Crear lista con los enlaces
# Esperar a que aparezcan los elementos de la página principal

elementos = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="headline"]/a')))
enlaces = [elem.get_attribute("href") for elem in elementos]

# Crear una lista para almacenar los datos
datos = []
n=0

# Recorrer los enlaces para extraer los autores
for enlace in enlaces:
    time.sleep(1)
    # Navegar a la página del artículo
    driver.get(enlace)
    # Esperar 10 segundos como máximo
    wait = WebDriverWait(driver, 10) 
    # Esperar a que aparezca el elemento del autor
    #elemento_autor = wait.until(EC.presence_of_element_located((By.XPATH, '//li[@class="byline"]/a')))
    #autor = elemento_autor.text

    fecha_elemento = driver.find_element(By.XPATH,'//div[@class="date"]')
    fecha = fecha_elemento.text

    titular_elemento = driver.find_element(By.XPATH,'//div[@class="headline"]/h1')
    titular = titular_elemento.text

    parrafos = driver.find_elements(By.XPATH,"//p[starts-with(@class,'p_')]")

    texto = ""
    # Iterar sobre cada elemento <p> y agregar su texto a la cadena de texto
    for parrafo in parrafos:
        texto += parrafo.text

    
    # Agregar los datos a la lista
    datos.append({'N':n,'Fecha': fecha, 'Titular': titular, 'Texto': texto})
    n=n+1 
    print("Fecha:", fecha)
    print("Titular:", titular)
    print("Texto:",texto)
# Cerrar el navegador
driver.quit()

# Crear un dataframe con los datos y exportarlos a un archivo Excel
df = pd.DataFrame(datos)
df.to_csv('datos.csv', index=False, encoding='utf8', sep="|")