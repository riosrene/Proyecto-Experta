from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome('Chromedriver.exe')
driver.get('https://experta.com.ar')
driver.maximize_window()
# time.sleep(2)

# Ingreso a la opcion SEGURO
option_seguro = driver.find_element_by_class_name("toggle-section").click()

# Ingreso a la Sub-opcion HOGAR
option_hogar = driver.find_element_by_id("menu-item-4677").click()

# Completar formulario o campos de la opcion HOGAR

# 1er Postal
cod_postal = driver.find_element_by_name('CP')
cod_postal.send_keys("1428")

# 2do Localidad
campo_localidad = driver.find_element_by_name('localidad')


# 3er Casa
# casa_point = driver.find_element_by_id("Casa")
# casa_point.send_keys()

# 4to Nombre
campo_nombre = driver.find_element_by_id("nombre")
campo_nombre.send_keys("Rene")


# 5to Apellido
campo_apellido = driver.find_element_by_id("apellido")
campo_apellido.send_keys("Rios")

# 6to E-Mail
campo_email = "rrr_c@hotmail.com"
campo_email = driver.find_element_by_id("email").send_keys(campo_email)

# 7mo Prefijo
campo_prefijo = "911"
campo_prefijo = driver.find_element_by_id("prefijo").send_keys(campo_prefijo)


# 8vo Telefono
campo_telefono = "21750014"
campo_telefono = driver.find_element_by_id("telefono").send_keys(campo_telefono)


# 9no Cotiza
campo_cotiza = driver.find_element_by_id("contratar-hogar")

time.sleep(2)


driver.quit()