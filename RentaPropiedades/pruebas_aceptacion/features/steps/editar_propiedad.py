import os
from behave import when, given, then
from selenium.webdriver.common.by import By  # importar clase by
from selenium.webdriver.support.ui import Select
import time

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))


@given(u'da clic en el botón de Editar')
def step_impl(context):
    context.driver.find_element(By.ID, 'id_editar').click()


@given(u'actualiza el precio "{precio}"')
def step_impl(context, precio):
    nuevo_precio = context.driver.find_element(By.ID, 'id_precio')
    # Limpia el campo
    nuevo_precio.clear()

    # Ingresa el nuevo valor
    nuevo_precio.send_keys(precio)


@given(u'actualiza el tipo de propiedad a "{tipo_prop}"')
def step_impl(context, tipo_prop):
    time.sleep(1)
    tipo = context.driver.find_element(By.ID, 'id_tipo')
    select = Select(tipo)
    select.select_by_index(int(tipo_prop))


@given(u'selecciona otra imagen de la propiedad "{nueva_img}"')
def step_impl(context, nueva_img):
    time.sleep(1)
    ruta_imagen = os.path.join(BASE_DIR, nueva_img.replace("\\", os.sep))
    # Encontrar el elemento de entrada de archivo
    upload_input = context.driver.find_element(By.ID, 'id_imagen')

    ruta_construida = f"Ruta de imagen construida: {ruta_imagen}"
    print(ruta_construida)  # Imprimir la ruta para depuración

    # Enviar la ruta absoluta al elemento de entrada de archivo
    upload_input.send_keys(ruta_imagen)

    # Esperar un momento para que el archivo se cargue
    time.sleep(2)


@when(u'presiona en el botón Guardar cambios')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.ID, "btn-guardar").click()


@then(u'puede ver el tipo de propiedad "{tipo_prop}" cambiado.')
def step_impl(context, tipo_prop):
    tipo = context.driver.find_element(By.XPATH, '//*[@id="tipo_prop"]').text
    assert tipo == tipo_prop, f"{tipo} no es {tipo_prop}"


@then(u'puede ver el mensaje siguiente "{mensaje}" en el campo del precio.')
def step_impl(context, mensaje):
    is_valid = (
        context.driver.find_element(By.ID, 'id_precio')
        .get_attribute('validationMessage')
        .strip()
    )
    assert is_valid == mensaje, (
        f"Expected '{mensaje}', but got '{is_valid}'")
