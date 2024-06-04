from behave import when, given, then
from selenium.webdriver.common.by import By  # importar clase by
import time


@given(u'escribe su correo "{email}" y su contraseña "{contrasenia}"')
def step_impl(context, email, contrasenia):
    time.sleep(1)
    context.driver.find_element(By.ID, 'username').send_keys(email)
    context.driver.find_element(By.ID, 'password').send_keys(contrasenia)


@given(u'presiona el botón de Log in')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.ID, 'btn-iniciar').click()


@given(u'presiona el botón de ver Perfil')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.ID, "btn-perfil").click()


@given(u'luego click en el botón editar perfil')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.ID, "btn-editar").click()


@when(u'presiona el botón Guardar cambios')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.ID, "btn-guardar").click()


@then(u'puede ver su nombre "{nombre}" cambiado.')
def step_impl(context, nombre):
    nombre_capturado = context.driver.find_element(
        By.CSS_SELECTOR, 'h5.title').text
    assert nombre_capturado == nombre
