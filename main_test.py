import data
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import phone_code
import UrbanRoutesPageLocators as URP
import urban_routes_page_methods as UrbanM


class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        chrome_options = Options()
        chrome_options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.implicitly_wait(10)
        cls.driver.get(data.urban_routes_url)
        cls.URP = URP.UrbanRoutesPageLocators
        cls.routes = UrbanM.UrbanRoutesPageMethods(cls.driver)

    # 1. Establecer direcciones de origen y destino.
    def test_set_route1(self):
        self.routes.set_from(data.address_from)
        self.routes.set_to(data.address_to)
        assert self.routes.get_from() == data.address_from
        assert self.routes.get_to() == data.address_to

        # 2. Seleccionar la tarifa "Comfort".
    def test_select_comfort_tariff2(self):
        self.routes.click_order_taxi_button()
        self.routes.click_comfort_tariff_button()
        comfort_tariff = self.driver.find_elements(*self.URP.comfort_tariff_button)
        assert "card" in self.driver.find_element(*self.URP.comfort_tariff_button).get_attribute("class")
        assert comfort_tariff[4].is_enabled()

        # 3. Rellenar el número de teléfono.
    def test_fill_phone_number3(self):
        self.routes.click_phone_number_field()
        self.routes.fill_in_phone_number()
        self.routes.click_next_button()
        self.routes.set_confirmation_code(phone_code.retrieve_phone_code(self.driver))
        self.routes.click_code_confirmation_button()
        phone_value = self.driver.find_element(*self.URP.phone_input).get_attribute("value")
        assert phone_value == data.phone_number

        # 4. Agregar una tarjeta de crédito.
    def test_add_credit_card4(self):
        self.routes.click_payment_method_field()
        self.routes.click_add_card_button()
        self.routes.enter_card_code()
        self.routes.press_tab_key()
        self.routes.click_add_button()
        card = self.driver.find_elements(*self.URP.card_added)[1]
        assert card.is_enabled()
        self.routes.click_card_close_button()

        # 5. Escribir un mensaje para el controlador.
    def test_write_message5(self):
        self.routes.click_order_taxi_button()
        self.routes.enter_new_message()
        assert self.driver.find_element(*self.URP.message).get_property('value') == data.message_for_driver

        # 6. Pedir una manta y pañuelos.
    def test_request_blanket_and_scarves6(self):
        self.routes.click_blanket_and_scarves_switch()
        check = self.driver.find_element(*self.URP.switch_check)
        assert check.is_selected() == True

    # 7. Pedir 2 helados.
    def test_request_icecream7(self):
        self.routes.click_comfort_tariff_button()
        self.routes.click_add_icecream()
        icecream_counter = int((self.driver.find_element(*self.URP.icecream_counter)).text)
        assert icecream_counter == 2

        # 8. Buscar un taxi.
    def test_search_taxi8(self):
        self.routes.click_order_a_taxi()
        assert self.driver.find_element(*self.URP.modal_opcional).is_displayed()

        # 9. Busqueda de conductor.
    def test_search_information_optional_modal9(self):
        self.routes.click_laboral_tariff_button()
        self.routes.click_order_a_taxi()
        self.routes.wait_opcional_modal()
        modal = self.routes.wait_search_driver_opcional_modal()
        assert modal.is_selected() == True

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()