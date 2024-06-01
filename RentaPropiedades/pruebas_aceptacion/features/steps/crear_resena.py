from behave import when, given, then
from selenium.webdriver.common.by import By #importar clase by
import time

@given(u'presiona el botón de lista de propiedades')
def step_impl(context):
    context.driver.find_element(By.ID, 'btn-propiedades').click()
    time.sleep(2)


@given(u'presiona el boton detalles de la propiedad "{datos_propiedad}"')
def step_impl(context, datos_propiedad):
    propiedades = context.driver.find_elements(By.CLASS_NAME, 'card')
    for propiedad in propiedades:
        if propiedad.find_element(By.CLASS_NAME, 'card-title').text == datos_propiedad:
            propiedad.find_element(By.CLASS_NAME, 'btn_redondo').click()
            break
    time.sleep(2)
    

@given(u'presiona el boton Reseñas de la propiedad')
def step_impl(context):
    context.driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div/div[3]/div/div[2]/div[2]/a').click()
    time.sleep(2)


@given(u'presiona el boton Agregar Reseña')
def step_impl(context):
    context.driver.find_element(By.CLASS_NAME, 'btn-success').click()
    time.sleep(2)


@given(u'escribe en la descripción "{mensaje_descripcion}"')
def step_impl(context, mensaje_descripcion):
    context.driver.find_element(By.ID, 'id_descripcion').send_keys(mensaje_descripcion)
    time.sleep(2)
    


@given(u'selecciona como calificación "{numero_estrellas}" estrellas')
def step_impl(context, numero_estrellas):
    if numero_estrellas == '1':
        context.driver.find_element(By.XPATH, '/html/body/div/div[2]/div/form/div/span[1]/i').click()
    elif numero_estrellas == '2':
        context.driver.find_element(By.XPATH, '/html/body/div/div[2]/div/form/div/span[2]/i').click()
    elif numero_estrellas == '3':
        context.driver.find_element(By.XPATH, '/html/body/div/div[2]/div/form/div/span[3]/i').click()
    elif numero_estrellas == '4':
        context.driver.find_element(By.XPATH, '/html/body/div/div[2]/div/form/div/span[4]/i').click()
    else:
        context.driver.find_element(By.XPATH, '/html/body/div/div[2]/div/form/div/span[5]/i').click()
    time.sleep(2)


@when(u'presiona el boton Guardar')
def step_impl(context):
    context.driver.find_element(By.CLASS_NAME, 'btn-info').click()
    time.sleep(2)

@when(u'presiona el boton Reseñas de la propiedad')
def step_impl(context):
    btns = context.driver.find_elements(By.CLASS_NAME, 'btn-primary')
    for btn in btns:
        if btn.text == "Reseñas de la propiedad":
            btn.click()
            break
    time.sleep(2)


@then(u've en la pagina "{texto}"')
def step_impl(context, texto):
    if texto in context.driver.find_element(By.XPATH, '/html/body/div/div[2]/div/form/div[5]').text:
        return True
    else:
        return False

@then(u've el mensaje en el campo descripcion "{alerta}"')
def step_impl(context, alerta):
    is_valid = context.driver.find_element(By.ID, 'id_descripcion').get_attribute('validationMessage')
    assert is_valid == alerta, f"Expected '{alerta}', but got '{is_valid}'"

@then(u've el mensaje de error "{mensaje}"')
def step_impl(context, mensaje):
    assert context.driver.find_element(By.ID, 'calificacion-error').text == mensaje