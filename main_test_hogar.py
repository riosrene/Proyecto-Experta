import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
# from Pages.pages_main import Pages


class main_test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('Chromedriver.exe')
        self.driver.get('https://experta.com.ar')
        self.driver.maximize_window()
        option_seguro = self.driver.find_element_by_class_name("toggle-section").click()
        option_hogar = self.driver.find_element_by_id("menu-item-4677").click()

    def test_hogar(self):
        # Completar formulario o campos de la opcion HOGAR
        # 1er Postal
        cod_postal = self.driver.find_element_by_name('CP')
        cod_postal.send_keys("1428")

        # 2do Localidad
        campo_localidad = self.driver.find_element_by_name('localidad')

        # 3er Casa
        # casa_point = driver.find_element_by_id("Casa")
        # casa_point.send_keys()

        # 4to Nombre
        campo_nombre = self.driver.find_element_by_id("nombre")
        campo_nombre.send_keys("Rene")

        # 5to Apellido
        campo_apellido = self.driver.find_element_by_id("apellido")
        campo_apellido.send_keys("Rios")

        # 6to E-Mail
        campo_email = "rrr_c@hotmail.com"
        campo_email = self.driver.find_element_by_id("email").send_keys(campo_email)

        # 7mo Prefijo
        campo_prefijo = "911"
        campo_prefijo = self.driver.find_element_by_id("prefijo").send_keys(campo_prefijo)

        # 8vo Telefono
        campo_telefono = "21750014"
        campo_telefono = self.driver.find_element_by_id("telefono").send_keys(campo_telefono)

        # 9no Cotiza
        campo_cotiza = self.driver.find_element_by_id("contratar-hogar")


if __name__ == '__main__':
    unittest.main()
