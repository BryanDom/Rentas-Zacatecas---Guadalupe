from behave import when, given, then
from selenium.webdriver.common.by import By  # importar clase by
import time


@given(u'da clic en el botón de eliminar')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.CLASS_NAME, 'fa-trash').click()


@when(u'presiona el botón de Cancelar')
def step_impl(context):
    context.driver.find_element(By.CLASS_NAME, 'btn-warning').click()
    time.sleep(2)


@then(u'vuelve y ve el título "{titulo}"')
def step_impl(context, titulo):
    txt_titulo = context.driver.find_element(By.CLASS_NAME, 'text-center').text
    assert titulo in txt_titulo, f'el titulo {titulo} no esta en {txt_titulo}'
    time.sleep(2)


@when(u'intento eliminar la propiedad con ID "{id_propiedad}" mediante URL')
def step_impl(context, id_propiedad):
    (context.driver.get(
        f'http://localhost:8000/Propiedades/'
        f'confirmacion_eliminacion_propiedad/{id_propiedad}'
    ))
    time.sleep(2)


@then(u'podra ver la confirmación "{mje_confirmacion}"')
def step_impl(context, mje_confirmacion):
    body_text = context.driver.find_element(By.TAG_NAME, 'body').text
    assert mje_confirmacion in body_text, \
        f'El mensaje "{mje_confirmacion}" no fue encontrado en la página.'
    time.sleep(2)


@when(u'presiona el botón de Eliminar Propiedad')
def step_impl(context):
    context.driver.find_element(By.CLASS_NAME, 'btn-danger').click()
    time.sleep(2)


@then(u'podra ver que la propiedad con ID "{id_propiedad}"'
      u'no debería estar en Mis propiedades')
def step_impl(context, id_propiedad):
    propiedades = context.driver.find_elements(By.CLASS_NAME, 'property-item')
    propiedad_encontrada = (
        any(id_propiedad in propiedad.get_attribute('data-id')
            for propiedad in propiedades)
    )
    assert not propiedad_encontrada, \
        f'La propiedad con ID {id_propiedad}' \
        f'todavía está presente en la lista de propiedades.'


@then(u'podra ver el botón Nueva Propiedad')
def step_impl(context):
    (context.driver
     .find_element(
         By.PARTIAL_LINK_TEXT,
         "Nueva Propiedad").click())
