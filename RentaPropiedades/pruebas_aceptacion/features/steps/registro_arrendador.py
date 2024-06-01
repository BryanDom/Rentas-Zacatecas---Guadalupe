from behave import when, given, then
from selenium import webdriver
from selenium.webdriver.common.by import By #importar clase by
import time


@given(u'que el arrendador ingresa a la url "{url}"')
def step_impl(context, url):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get(url)


@given(u'presiona el botón Crear cuenta arrendador')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.PARTIAL_LINK_TEXT, "Crear cuenta arrendador").click()


@given(u'escribe su ocupación "{ocupacion}"')
def step_impl(context, ocupacion):
    oc = context.driver.find_element(By.ID, 'id_ocupacion').send_keys(ocupacion)


@given(u'escribe sus preferencias de arrendatarios "{preferencias}"')
def step_impl(context, preferencias):
    pr = context.driver.find_element(By.ID, 'id_preferencias_arrendatarios').send_keys(preferencias)


@given(u'no completa el campo de preferencias de arrendamiento ""')
def step_impl(context):
    pr = context.driver.find_element(By.ID, 'id_preferencias_arrendatarios').send_keys("")

@then(u've la alerta "{alerta}"')
def step_impl(context, alerta):
    is_valid = context.driver.find_element(By.ID, 'id_correo').get_attribute('validationMessage')
    assert is_valid == alerta, f"Expected '{alerta}', but got '{is_valid}'"

@given(u'no escribe su teléfono')
def step_impl(context):
    tel = context.driver.find_element(By.ID, 'id_telefono').send_keys("")


@then(u've la alerta de error "{alerta}"')
def step_impl(context, alerta):
    is_valid = context.driver.find_element(By.ID, 'id_telefono').get_attribute('validationMessage')
    assert is_valid == alerta, f"Expected '{alerta}', but got '{is_valid}'"