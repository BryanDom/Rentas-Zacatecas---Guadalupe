from behave import when, given, then
from selenium.webdriver.common.by import By #importar clase by
import time


@when(u'presiona el botón de ver Perfil')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.ID, "btn-perfil").click()


@then(u'puede ver su nombre completo "{nombre}"')
def step_impl(context, nombre):
    nombre_capturado = context.driver.find_element(By.CSS_SELECTOR, 'h5.title').text
    assert nombre_capturado == nombre

@then(u'puede ver su edad "{edad}"')
def step_impl(context, edad):
   edad_cap = context.driver.find_element(By.CSS_SELECTOR, "p.description:nth-child(3)").text
   assert edad in edad_cap


@then(u'puede ver su sexo "{sexo}"')
def step_impl(context, sexo):
   sexo_cap = context.driver.find_element(By.CSS_SELECTOR, "p.description:nth-child(4)").text 
   assert sexo in sexo_cap


@then(u'puede ver su universidad actual "{universidad}"')
def step_impl(context, universidad):
   universidad_cap = context.driver.find_element(By.CSS_SELECTOR, "p.description:nth-child(5)").text 
   assert universidad in universidad_cap


@then(u'puede ver su teléfono "{num}"')
def step_impl(context, num):
   num_cap = context.driver.find_element(By.CSS_SELECTOR, "p.description:nth-child(6)").text 
   assert num in num_cap


@then(u'puede ver sus preferencias de búsqueda "{preferencias}"')
def step_impl(context, preferencias):
   preferencias_cap = context.driver.find_element(By.CSS_SELECTOR, "p.description:nth-child(7)").text 
   assert preferencias in preferencias_cap


@then(u'puede ver sus pasatiempos "{pasatiempos}"')
def step_impl(context, pasatiempos):
   pasatiempos_cap = context.driver.find_element(By.CSS_SELECTOR, "p.description:nth-child(8)").text 
   assert pasatiempos in pasatiempos_cap


@then(u'puede ver los botones para editar perfil y contacto')
def step_impl(context):
    # Buscar botón de editar perfil
    btn_editar = context.driver.find_element(By.ID, "btn-editar")

    # Buscar botones de contacto 
    btn_telefono = context.driver.find_element(By.ID, "id_telefono")
    btn_whatsapp = context.driver.find_element(By.ID, "id_whatsapp")
    btn_email = context.driver.find_element(By.ID, "id_correo")

    # Validar que se encuentren todos los btnes
    assert btn_editar 
    assert btn_telefono
    assert btn_whatsapp  
    assert btn_email
