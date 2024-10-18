from selenium.webdriver import Keys
import data
import time
import UrbanRoutesPageLocators as URP
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class UrbanRoutesPageMethods:
    def __init__(self, driver):
        self.URP = URP.UrbanRoutesPageLocators
        self.driver = driver

    # Métodos de acciones en la página
      #Metodos para la prueba 1
    def set_from(self, from_address):
        self.driver.find_element(*self.URP.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.URP.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.URP.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.URP.to_field).get_property('value')

    def click_order_taxi_button(self):
        self.driver.find_element(*self.URP.order_taxi_button).click()

    # Metodos para la prueba 2
    def click_comfort_tariff_button(self):
        tariff = self.driver.find_elements(*self.URP.comfort_tariff_button)
        tariff[4].click()

    # Metodos para la prueba 3
    def click_phone_number_field(self):
        self.driver.find_element(*self.URP.telephone).click()

    def fill_in_phone_number(self):
        self.driver.find_element(*self.URP.phone).send_keys(data.phone_number)

    def click_next_button(self):
        self.driver.find_element(*self.URP.button_phone).click()

    def set_confirmation_code(self, code):
        self.driver.find_element(*self.URP.code).send_keys(code)

    def click_code_confirmation_button(self):
        self.driver.find_element(*self.URP.code_confirmation_).click()

    # Metodos para la prueba 4
    def click_payment_method_field(self):
        self.driver.find_element(*self.URP.payment_method).click()

    def click_add_card_button(self):
        self.driver.find_element(*self.URP.add_card).click()
        WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(self.URP.card_number_field)
                ).send_keys(data.card_number)

    def enter_card_number(self):
        self.driver.find_element(*self.URP.card_number_field).send_keys(data.card_number)

    def enter_card_code(self):
        self.driver.find_element(*self.URP.card_code_field).send_keys(data.card_code)

    def press_tab_key(self):
        self.driver.find_element(*self.URP.card_code_field).send_keys(Keys.TAB)

    def click_add_button(self):
        add = self.driver.find_element(*self.URP.add_button).click()
        print(add)

    def click_card_close_button(self):
        self.driver.find_element(*self.URP.card_close_button).click()

    # Metodos para la prueba 5
    def enter_new_message(self):
        self.driver.find_element(*self.URP.message).send_keys(data.message_for_driver)

    # Metodos para la prueba 6
    def click_blanket_and_scarves_switch(self):
        self.driver.find_element(*self.URP.blanket_and_scarves_switch).click()

    # Metodos para la prueba 7
    def click_add_icecream(self):
        self.driver.find_element(*self.URP.add_icecream).click()
        self.driver.find_element(*self.URP.add_icecream).click()

    # Metodos para la prueba 8
    def click_order_a_taxi(self):
        self.driver.find_element(*self.URP.order_a_taxi).click()

    def wait_opcional_modal(self):
        self.driver.find_element(*self.URP.modal_opcional)

    # Metodos para la prueba 9
    def driver_information(self):
        self.driver.find_element(*self.URP.driver_information)
        self.driver.find_element(*self.URP.car_draw)