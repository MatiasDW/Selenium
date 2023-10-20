from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pandas as pd

# Define la ruta al driver de Edge
driver_path = 'C:\\Users\\Matias Davila\\OneDrive - DISTRIBUIDORA Y COMERCIALIZADORA OPEN\\Documentos\\Matias\\msedgedriver.exe'

# Crea una instancia del servicio Edge
edge_service = Service(driver_path)

# Crea una instancia del driver de Edge utilizando el servicio
driver = webdriver.Edge(service=edge_service)  

# Iniciarla en la pantalla 2
driver.set_window_position(2000, 0)
driver.maximize_window()
time.sleep(5)

# Inicializamos el navegador
driver.get('https://eltiempo.es')

# Espera hasta que el botón esté presente
wait = WebDriverWait(driver, 10)
button = wait.until(EC.presence_of_element_located((By.ID, "didomi-notice-agree-button")))

# Hacer clic en el botón
button.click()

# Espera hasta que el campo de búsqueda esté presente
search_bar = wait.until(EC.presence_of_element_located((By.ID, "term")))

# Ingresa 'Madrid' en el campo de búsqueda
search_term = 'Madrid'
search_bar.send_keys(search_term)

# Espera hasta que el resultado de la búsqueda "Madrid" esté presente y haz clic en él
search_result = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".poi-title")))
search_result.click()

while True:
    time.sleep(10)
