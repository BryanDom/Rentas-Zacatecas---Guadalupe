from behave import when, given, then
from selenium import webdriver
from selenium.webdriver.common.by import By #importar clase by
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

@when(u'presiona el botón de lista de propiedades')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.ID, "btn-propiedades").click()

@then(u'puede ver una lista de propiedades con información.')
def step_impl(context):
    # Recolectamos todos los elementos h5 y guardamos en una lista por Tag name
    ubicaciones = context.driver.find_elements(By.TAG_NAME, 'h5')
    
    # Recolectamos todos los elementos strong que contienen el tipo y el precio
    tipos_precios = context.driver.find_elements(By.TAG_NAME, 'strong')
    
    # Verificamos que las listas no estén vacías (condición de falla)
    assert len(ubicaciones) > 0, "No se encontraron propiedades"

    # Extraemos los tipos y precios de los elementos strong
    tipos = []
    precios = []
    #inicia desde 0 y incrementa dos en dos
    #porque en 2, bueno el 0 que es par guardo el tipo de casa y el impar este caso el 1
    #guardo el precio y asi sucesivamente con cada propiedad que pasa. Lo vamos guardando
    #en una lista
    for i in range(0, len(tipos_precios), 2):
        tipos.append(tipos_precios[i].text)
        precios.append(tipos_precios[i + 1].text)

    # Verificamos que cada propiedad tenga una ubicación, tipo y precio
    for ubicacion in ubicaciones:
        assert ubicacion.text, "No existe propiedad"

    for tipo in tipos:
        assert tipo, "No existe propiedad"

    #para verificar qu es cierto lo del precio, tiene que iniciar con $
    for precio in precios:
        assert precio.startswith('$'), "No existe propiedad"