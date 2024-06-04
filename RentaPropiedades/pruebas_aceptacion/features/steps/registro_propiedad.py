import os
from behave import when, given, then
from selenium.webdriver.common.by import By  # importar clase by
from selenium.webdriver.support.ui import Select
import time

# Ruta base del proyecto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))


@given(u'da clic en Nueva Propiedad')  # noqa: F811
def step_impl(context):
    time.sleep(1)
    (context.driver
     .find_element(
         By.PARTIAL_LINK_TEXT,
         "Nueva Propiedad").click())


@given(u'escribe la descripción de la propiedad "{descripcion}"')
def step_impl(context, descripcion):  # noqa: F811
    context.driver.find_element(By.ID, 'id_descripcion').send_keys(descripcion)


@given(u'escribe el precio "{precio}"')
def step_impl(context, precio):  # noqa: F811
    context.driver.find_element(By.ID, 'id_precio').send_keys(precio)


@given(u'selecciona el tipo de propiedad "{tipo_propiedad}"')
def step_impl(context, tipo_propiedad):  # noqa: F811
    time.sleep(1)
    tipo = context.driver.find_element(By.ID, 'id_tipo')
    select = Select(tipo)
    select.select_by_index(int(tipo_propiedad) - 1)


@given(u'escribe la calle "{nombre_calle}"')
def step_impl(context, nombre_calle):  # noqa: F811
    context.driver.find_element(By.ID, 'calle').send_keys(nombre_calle)


@given(u'escribe el número "{numero}"')
def step_impl(context, numero):  # noqa: F811
    context.driver.find_element(By.ID, 'numero').send_keys(numero)


@given(u'selecciona el municipio "{municipio}"')
def step_impl(context, municipio):  # noqa: F811
    time.sleep(1)
    zac = context.driver.find_element(By.ID, 'municipio')
    select = Select(zac)
    select.select_by_visible_text(municipio)


@given(u'selecciona la colonia "{colonia}"')
def step_impl(context, colonia):  # noqa: F811
    time.sleep(1)
    col = context.driver.find_element(By.ID, 'colonia')
    select = Select(col)
    select.select_by_visible_text(colonia)


@given(u'selecciona la primera imagen de la propiedad "{foto_1}"')
def step_impl(context, foto_1):  # noqa: F811
    time.sleep(1)
    ruta_imagen = os.path.join(BASE_DIR, foto_1.replace("\\", os.sep))
    # Encontrar el elemento de entrada de archivo
    upload_input = context.driver.find_element(By.ID, 'id_imagen_0-imagen')

    ruta_construida = f"Ruta de imagen construida: {ruta_imagen}"
    print(ruta_construida)  # Imprimir la ruta para depuración

    # Enviar la ruta absoluta al elemento de entrada de archivo
    upload_input.send_keys(ruta_imagen)

    # Esperar un momento para que el archivo se cargue
    time.sleep(2)


@given(u'selecciona la segunda imagen de la propiedad "{foto_2}"')
def step_impl(context, foto_2):  # noqa: F811
    time.sleep(1)
    ruta_imagen = os.path.join(BASE_DIR, foto_2.replace("\\", os.sep))
    # Encontrar el elemento de entrada de archivo
    upload_input = context.driver.find_element(By.ID, 'id_imagen_1-imagen')

    ruta_construida = f"Ruta de imagen construida: {ruta_imagen}"
    print(ruta_construida)  # Imprimir la ruta para depuración

    # Enviar la ruta absoluta al elemento de entrada de archivo
    upload_input.send_keys(ruta_imagen)

    # Esperar un momento para que el archivo se cargue
    time.sleep(2)


@given(u'palomea la opción de servicios incluidos')
def step_impl(context):  # noqa: F811
    checkbox = context.driver.find_element(By.ID, 'id_serviciosIncluidos')
    checkbox.click()


@given(u'después palomea la opción de info verídica')
def step_impl(context):  # noqa: F811
    checkbox = context.driver.find_element(By.ID, 'GFG')
    checkbox.click()


@when(u'presiona el botón Agregar')
def step_impl(context):  # noqa: F811
    time.sleep(1)
    context.driver.find_element(By.CLASS_NAME, "btn-success").click()


@then(u'puede ver el siguiente mensaje "{mensaje}"')
def step_impl(context, mensaje):  # noqa: F811
    time.sleep(1)
    exito = context.driver.find_element(By.ID, 'mjeExito').text
    assert mensaje == exito, f"El mensaje {mensaje} no se encuentra en {exito}"


@then(u'puede ver el siguiente mensaje de error "{error}"')
def step_impl(context, error):  # noqa: F811
    time.sleep(1)
    mje = context.driver.find_element(By.ID, 'mjeError').text
    assert error == mje, f"El mensaje {error} no se encuentra en {mje}"


@then(u'puede ver el mensaje de error "{error}"')
def step_impl(context, error):  # noqa: F811
    is_valid = (
        context.driver.find_element(By.ID, 'id_precio')
        .get_attribute('validationMessage').strip()
    )
    assert is_valid == error, f"Expected '{error}', but got '{is_valid}'"


@then(u'puede ver la siguiente alerta "{alerta}"')
def step_impl(context, alerta):  # noqa: F811
    is_valid = (
        context.driver.find_element(By.ID, 'id_imagen_0-imagen')
        .get_attribute('validationMessage').strip()
    )
    assert is_valid == alerta


@then(u'puede ver la siguiente alerta de seguridad "{alerta_seguridad}"')
def step_impl(context, alerta_seguridad):  # noqa: F811
    is_valid = (
        context.driver.find_element(By.ID, 'GFG')
        .get_attribute('validationMessage').strip()
    )
    assert is_valid == alerta_seguridad


@then(u've el mensaje "{mje_seleccion}"')
def step_impl(context, mje_seleccion):  # noqa: F811
    is_valid = (
        context.driver.find_element(By.ID, 'municipio')
        .get_attribute('validationMessage')
        .strip()
    )
    assert is_valid == mje_seleccion, (
        f"Expected '{mje_seleccion}', but got '{is_valid}'")
