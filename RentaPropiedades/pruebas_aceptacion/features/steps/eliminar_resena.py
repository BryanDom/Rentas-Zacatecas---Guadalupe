from behave import when, given, then
from selenium.webdriver.common.by import By  # importar clase by
import time


@given(u'presiona el boton de Eliminar reseña')
def step_impl(context):  # noqa: F811
    context.driver.find_element(By.CLASS_NAME, 'btn-danger').click()
    time.sleep(2)


@when(u'presiona el boton de eliminar confirmando su eliminación')
def step_impl(context):  # noqa: F811
    context.driver.find_element(By.CLASS_NAME, 'btn-danger').click()
    time.sleep(2)


@when(u'presiona el boton de Cancelar')
def step_impl(context):  # noqa: F811
    context.driver.find_element(By.CLASS_NAME, 'btn-warning').click()
    time.sleep(2)


@then(u'podra observar el boton Agregar Reseña')
def step_impl(context):  # noqa: F811
    assert context.driver.find_element(
        By.CLASS_NAME, 'btn-success').text == 'Agregar Reseña'
    time.sleep(2)
