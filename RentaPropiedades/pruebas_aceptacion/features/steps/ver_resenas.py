from behave import given, then
from selenium.webdriver.common.by import By  # importar clase by
import time


@given(u'presiona el botón de mis propiedades')
def step_impl(context):  # noqa: F811
    context.driver.find_element(
        By.XPATH, '/html/body/div/div[1]/div[1]/ul/li[2]/a').click()
    time.sleep(2)


@given(u'presiona el boton detalles de mi propiedad "{datos_propiedad}"')
def step_impl(context, datos_propiedad):  # noqa: F811
    contenedores_propiedades = context.driver.find_elements(
        By.CLASS_NAME, 'd-flex')
    for propiedad in contenedores_propiedades:
        titulo_propiedad = propiedad.find_element(By.CLASS_NAME, 'card-title')
        if titulo_propiedad.text == datos_propiedad:
            propiedad.find_element(By.CLASS_NAME, 'btn_redondo').click()
            break
    time.sleep(2)


@then(u've el titulo "{titulo}"')
def step_impl(context, titulo):  # noqa: F811
    texto_titulo = context.driver.find_element(
        By.CLASS_NAME, 'text-center').text
    assert titulo in texto_titulo, \
        f'el titulo {titulo} no esta en {texto_titulo}'
    time.sleep(2)
