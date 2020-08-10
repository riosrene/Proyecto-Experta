from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome('Chromedriver.exe')
driver.get('https://experta.com.ar')
driver.maximize_window()
time.sleep(5)

# Ingreso a la opcion SEGURO y luego a la sub opcion Accidentes Personales

option_seguro = driver.find_element_by_class_name("toggle-section").click()
option_acciperso = driver.find_element_by_id("menu-item-3661").click()

# Ingreso a la sub opcion Accidentes Personales y llenar el formulario

# 1er campo Actividad
act_Dropdown = Select(driver.find_element_by_id("ap-actividades"))
act_Dropdown.select_by_value("7")

# 2do campo cantidad de personas
cantperson_Dropdown = Select(driver.find_element_by_id("cantidad"))
cantperson_Dropdown.select_by_index(3)

# 3er campo Periodo
periodo_Dropdown = Select(driver.find_element_by_id("ap-periodo"))
periodo_Dropdown.select_by_visible_text("Anual")

# 4to campo fecha desde
fechadesde_box = driver.find_element_by_id("ap-desde").click()
# fechadesde_box.send_keys("08/08/20")


# 5to campo fecha hasta
fechahasta_box = driver.find_element_by_id("ap-hasta").click()
# fechahasta_box.send_keys("08/08/21")
time.sleep(5)

# 6to Nombre
campo_nombre = driver.find_element_by_id("ap-nombre")
campo_nombre.send_keys("Rene")


# 7mo Apellido
campo_apellido = driver.find_element_by_id("ap-apellido")
campo_apellido.send_keys("Rios")

# 8vo E-Mail
campo_email = "rrr_c@hotmail.com"
campo_email = driver.find_element_by_id("ap-email").send_keys(campo_email)

# 9mo Prefijo
campo_prefijo = "911"
campo_prefijo = driver.find_element_by_id("ap-prefijo").send_keys(campo_prefijo)


# 10mo Telefono
campo_telefono = "21750014"
campo_telefono = driver.find_element_by_id("ap-telefono").send_keys(campo_telefono)


# 9no Cotiza
campo_cotiza = driver.find_element_by_id("contratar-ap")

time.sleep(2)

driver.quit()