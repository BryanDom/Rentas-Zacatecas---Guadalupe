from behave import when, given, then
from selenium.webdriver.common.by import By #importar clase by
import time

@given(u'presiona el botón de ver Perfil arrendador')
def step_impl(context):
    perfil = context.driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/ul/li[1]/a').click()


@given(u'luego click en el botón editar perfil arrendador')
def step_impl(context):
    editar = context.driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div/div/div[4]/form/span/a').click()

@when(u'da click en el botón Guardar cambios')
def step_impl(context):
    guardar = context.driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div/form/span/button').click()