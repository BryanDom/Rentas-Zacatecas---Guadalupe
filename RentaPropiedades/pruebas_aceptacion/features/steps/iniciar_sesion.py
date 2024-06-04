from behave import when, then
from selenium.webdriver.common.by import By  # importar clase by
import time


@when(u'presiona el botón de Log in')
def step_impl(context):
    context.driver.find_element(By.ID, 'btn-iniciar').click()
    time.sleep(2)


@then(u've la alerta: "{mensaje_alerta}"')
def stem_impl(context, mensaje_alerta):
    assert context.driver.find_element(
        By.CLASS_NAME, 'alert').text == mensaje_alerta
