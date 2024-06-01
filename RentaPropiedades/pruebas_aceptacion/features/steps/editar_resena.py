from behave import when, given, then
from selenium.webdriver.common.by import By #importar clase by
import time

@given(u'presiona el boton de Editar reseña')
def step_impl(context):
    context.driver.find_element(By.CLASS_NAME, 'btn-success').click()
    time.sleep(2)


@given(u'modifica la descripción con el texto "{mensaje}"')
def step_impl(context, mensaje):
    descripcion = context.driver.find_element(By.ID, 'id_descripcion')
    descripcion.clear()
    descripcion.send_keys(mensaje)
    time.sleep(2)

@given(u'modifica la calificación asignando "{num_estrellas}" estrellas a la reseña')
def step_impl(context, num_estrellas):
    if num_estrellas == '1':
        context.driver.find_element(By.XPATH, '/html/body/div/div[2]/div/form/div/span[1]/i').click()
    elif num_estrellas == '2':
        context.driver.find_element(By.XPATH, '/html/body/div/div[2]/div/form/div/span[2]/i').click()
    elif num_estrellas == '3':
        context.driver.find_element(By.XPATH, '/html/body/div/div[2]/div/form/div/span[3]/i').click()
    elif num_estrellas == '4':
        context.driver.find_element(By.XPATH, '/html/body/div/div[2]/div/form/div/span[4]/i').click()
    else:
        context.driver.find_element(By.XPATH, '/html/body/div/div[2]/div/form/div/span[5]/i').click()
    time.sleep(2)

@given(u'modifica la descripción dejandola vacia')
def step_impl(context):
    descripcion = context.driver.find_element(By.ID, 'id_descripcion')
    descripcion.clear()
    time.sleep(2)

@then(u've la reseña modificada con la descripción: "{descripcion}"')
def step_impl(context, descripcion):
    assert context.driver.find_element(By.CLASS_NAME, 'contenedor_descipcion').text == descripcion
    time.sleep(2)


@then(u've la reseña modificada con la calificacion de "{num_estrellas}" estrellas')
def step_impl(context, num_estrellas):
    contenedor_estrellas = context.driver.find_element(By.CLASS_NAME, 'contenedor_estrellas')
    estrellas_reseña = len(contenedor_estrellas.find_elements(By.CLASS_NAME, 'fas'))
    assert estrellas_reseña == int(num_estrellas), f"El numero de estrellas {estrellas_reseña} no es igual a las esperadas {num_estrellas}"