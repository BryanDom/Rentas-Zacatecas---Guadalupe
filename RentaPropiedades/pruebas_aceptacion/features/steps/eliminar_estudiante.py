from behave import when, given, then
from selenium.webdriver.common.by import By  # importar clase by
import time


@given(u'presiona el botón Eliminar Perfil')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.ID, "btn-eliminar").click()


@when(u'presiona el botón Eliminar Perfil')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.ID, "id_eliminar").click()


@given(u'puede ver el mensaje "{mensaje}"')
def step_impl(context, mensaje):
    mensaje_cap = context.driver.find_element(By.TAG_NAME, 'h1').text
    assert mensaje_cap == mensaje


@then(u'puede ver el mensaje "{mensaje}".')
def step_impl(context, mensaje):
    time.sleep(1)
    mensaje_exito = context.driver.find_element(
        By.XPATH, "/html/body/div/div[2]/p/strong").text
    assert mensaje in mensaje_exito
