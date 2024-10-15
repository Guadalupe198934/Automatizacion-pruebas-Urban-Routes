Urban Routes Automation Test
Descripción:
Este proyecto consiste en pruebas automatizadas para la aplicación web Urban Routes, utilizando Selenium WebDriver con Python. Este proyecto realiza pruebas automatizadas para verificar el funcionamiento correcto de las principales caracteristicas de la aplicación, como la búsqueda de rutas, la selección de tarifas, el ingreso de datos como el número telefónico, el proceso de pago y la interacción con el controlador.

Requisitos:
Python 3
Selenium WebDriver
Chrome WebDriver
Pytest
PyCharm (Opcional)
Instalación
Clona este repositorio a tu directorio local.
git clone git@github.com:Guadalupe198934/qa-project-Urban-Routes-es.git
Asegúrate de tener Python instalado.
Se recomienda la instalación del entorno "PyCharm" para la ejecución de las pruebas
Descarga Chrome WebDriver y configura la ruta en tu sistema.
Instala Selenium (Verifica que la version sea compatible con tu version de Chrome)
pip install selenium
instala "pytest" utilizando pip en la terminal de comandos:
pip install pytest

Contenido del proyecto:
"data.py": Archivo de configuración con los datos de prueba
"UrbanRoutesPAgeLocators": Archivo que contiene los localizadores de todos los metodos utilizados
"main_test.py": Archivo principal que contiene las pruebas automatización para el flujo de la aplicación.
"urban_routes_page_methods.py": Archivo que define los metodos de "UrbanRoutesPage".
"phone_code.py": Archivo que contiene la funcion para establecer la confirmación del código del telefono.

Ejecución de Pruebas
Para ejecutar las pruebas, simplemente utiliza el comando pytest en la terminal de comandos:
pytest
Asegúrate de estar en el directorio raíz del proyecto para ejecutar el comando. Otra alternativa es utilizar el entorno "PyCharm" para correr las pruebas con Pytest.

Pruebas Disponibles
1.-Establecer las direcciones de origen y destino.
2.-Seleccionar la tarifa "Comfort".
3.-Rellenar el número de teléfono.
4.-Agregar tarjeta de crédito.
5.-Escribir un mensaje para el controlador.
6.-Pedir manta y pañuelos.
7.-Pedir helados.
8.-Buscar un taxi.
9.-Aparecerá el modal de búsqueda de conductor 