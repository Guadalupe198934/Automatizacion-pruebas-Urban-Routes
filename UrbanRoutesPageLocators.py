from selenium.webdriver.common.by import By

class UrbanRoutesPageLocators:
    #Prueba 1. Localizadores para la Configurar la dirección
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    #Prueba 2. Localizadores para Seleccionar la tarifa Comfort.
    order_taxi_button = (By.XPATH, '//*[text()="Pedir un taxi"]')
    comfort_tariff_button = (By.CLASS_NAME, 'tcard')
    #Prueba 3.Localizadores para Rellenar el número de teléfono.
    telephone = (By.CLASS_NAME, "np-button")
    phone = (By.ID, 'phone')
    button_phone = (By.XPATH, '//*[text()="Siguiente"]')
    code = (By.ID, 'code')
    code_confirmation_ = (By.XPATH, '//*[text()="Confirmar"]')
    # Prueba 4.Localizadores para Agregar una tarjeta de crédito.
    payment_method = (By.CLASS_NAME, "pp-button")
    add_card = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[3]/div/img')
    card_added = (By.CLASS_NAME, 'pp-row')
    card_number_field = (By.NAME,'number')
    card_code_field = (By.NAME, 'code')
    add_button = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/form/div[3]/button[1]')
    card_close_button = (By.CSS_SELECTOR, '.payment-picker.open .modal .section.active .close-button')
    # Prueba 5.Localizadores para Escribir un mensaje para el controlador.
    message = (By.ID, 'comment')
    # Prueba 6.Localizadores para Pedir una manta y pañuelos
    blanket_and_scarves_switch = (By.CLASS_NAME, "switch")
    switch_check = (By.CLASS_NAME, "switch-input")
    # Prueba 7.Localizadores para Pedir 2 helados.
    add_icecream = (By.CLASS_NAME, "counter-plus")
    icecream_counter = (By.CLASS_NAME, "counter-value")
    # Prueba 8.Localizadores para Aparece el modal para buscar un taxi.
    order_a_taxi = (By.CLASS_NAME, "smart-button-wrapper")
    modal_opcional = (By.XPATH,'//*[@id="root"]/div/div[5]/div[2]/div[2]/div[1]')
    # Prueba 9.Localizadores para Busqueda de conductor.
    driver_information = (By.CSS_SELECTOR, '[style="cursor: default;"]')
    car_draw = (By.CSS_SELECTOR, '[alt="Car"]')

