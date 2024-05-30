from behave import when, given, then
from selenium.webdriver.common.by import By #importar clase by
import time

@given(u'presiona el botón Eliminar Perfil arrendador')
def step_impl(context):
    eliminar = context.driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div/form/span/a[2]').click()

@when(u'presiona el botón Eliminar Perfil arrendador')
def step_impl(context):
    eliminar = context.driver.find_element(By.XPATH, '/html/body/div/div[2]/div/span/a[2]').click()