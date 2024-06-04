from behave import when, given, then
from selenium import webdriver
from selenium.webdriver.common.by import By  # importar clase by
import time
import os

# Ruta base del proyecto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))


@given(u'que el estudiante ingresa a la url "{url}"')
def step_impl(context, url):  # noqa: F811
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get(url)


@given(u'presiona el botón Crear cuenta estudiante')
def step_impl(context):  # noqa: F811
    time.sleep(2)
    # By.LINK_TEXT requiere que coincida exactamente el texto,
    # mientras que By.PARTIAL_LINK_TEXT permite coincidencias parciales,
    # lo cual es más adecuado para este caso dado que el texto completo del
    # botón incluye cosas extras como la clase.
    context.driver.find_element(
        By.PARTIAL_LINK_TEXT, "Crear cuenta estudiante").click()


@given(u'presiona el botón Siguiente')
def step_impl(context):  # noqa: F811
    time.sleep(2)
    context.driver.find_element(By.CLASS_NAME, "btn_siguiente").click()


@given(u'presiona el botón Aceptar y continuar')
def step_impl(context):  # noqa: F811
    time.sleep(2)
    context.driver.find_element(By.ID, "btn-aceptar").click()


@given(u'escribe su nombre "{nombre}", '
       u'sus apellidos "{apellidos}", su edad "{edad}"')
def step_impl(context, nombre, apellidos, edad):  # noqa: F811
    time.sleep(2)
    nom = context.driver.find_element(By.ID, 'id_nombre')
    nom.clear()
    nom.send_keys(nombre)
    ap = context.driver.find_element(By.ID, 'id_apellidos')
    ap.clear()
    ap.send_keys(apellidos)
    ed = context.driver.find_element(By.ID, 'id_edad')
    ed.clear()
    ed.send_keys(edad)


@given(u'selecciona su sexo "{sexo}"')
def step_impl(context, sexo):  # noqa: F811
    time.sleep(2)
    radio_button = context.driver.find_element(
        By.XPATH, '//input[@value="' + sexo + '"]')
    radio_button.click()


@given(u'selecciona su foto de perfil "{foto}"')
def step_impl(context, foto):  # noqa: F811
    time.sleep(2)
    ruta_imagen = os.path.join(BASE_DIR, foto.replace("\\", os.sep))
    # Encontrar el elemento de entrada de archivo
    upload_input = context.driver.find_element(By.ID, 'id_foto_perfil')

    # Imprimir la ruta para depuración
    print(f"Ruta de imagen construida: {ruta_imagen}")
    # Enviar la ruta absoluta al elemento de entrada de archivo
    upload_input.send_keys(ruta_imagen)

    # Esperar un momento para que el archivo se cargue
    time.sleep(2)


@given(u'escribe su universidad actual "{universidad}"')
def step_impl(context, universidad):  # noqa: F811
    unive = context.driver.find_element(By.ID, 'id_universidad_actual')
    unive.clear()
    unive.send_keys(universidad)


@given(u'escribe su teléfono "{telefono}"')
def step_impl(context, telefono):  # noqa: F811
    tel = context.driver.find_element(By.ID, 'id_telefono')
    tel.clear()
    tel.send_keys(telefono)


@given(u'escribe su WhatsApp "{whatsapp}"')
def step_impl(context, whatsapp):  # noqa: F811
    whats = context.driver.find_element(By.ID, 'id_whatsapp')
    whats.clear()
    whats.send_keys(whatsapp)


@given(u'escribe su correo "{correo}"')
def step_impl(context, correo):  # noqa: F811
    corr = context.driver.find_element(By.ID, 'id_correo')
    corr.clear()
    corr.send_keys(correo)


@given(u'escribe sus preferencias de búsqueda "{preferencias}"')
def step_impl(context, preferencias):  # noqa: F811
    pref = context.driver.find_element(By.ID, 'id_preferencias_busqueda')
    pref.clear()
    pref.send_keys(preferencias)


@given(u'escribe sus pasatiempos "{pasatiempos}"')
def step_impl(context, pasatiempos):  # noqa: F811
    pasa = context.driver.find_element(By.ID, 'id_pasatiempos')
    pasa.clear()
    pasa.send_keys(pasatiempos)


@given(u'puede ver el mensaje del compromiso del sistema')
def step_impl(context):  # noqa: F811
    mensaje_compromiso = context.driver.find_element(
        By.XPATH, '/html/body/div/div/p[2]').text
    compromiso_esperado = (
        "Nuestro compromiso"
    )
    assert compromiso_esperado in mensaje_compromiso


@given(u'ingresa la contraseña "{contrasenia}"')
def step_impl(context, contrasenia):  # noqa: F811
    context.driver.find_element(By.ID, 'id_password').send_keys(contrasenia)


@given(u'para confirmar nuevamente ingresa la contraseña "{contrasenia}"')
def step_impl(context, contrasenia):  # noqa: F811
    context.driver.find_element(By.ID, 'id_re_pass').send_keys(contrasenia)


@given(u'no completa el campo de pasatiempos "{campo}"')
def step_impl(context, campo):  # noqa: F811
    context.driver.find_element(By.ID, 'id_pasatiempos').send_keys(campo)


@when(u'presiona el botón Continuar')
def step_impl(context):  # noqa: F811
    context.driver.find_element(By.ID, "btn-crearContra").click()


@when(u'presiona el botón Siguiente')
def step_impl(context):  # noqa: F811
    time.sleep(1)
    context.driver.find_element(By.CLASS_NAME, "btn_siguiente").click()


@then(u'puede ver el mensaje "{mensaje}"')
def step_impl(context, mensaje):  # noqa: F811
    exito = context.driver.find_element(
        By.XPATH, '/html/body/div/div[2]/div[1]/div/h1').text
    assert mensaje == exito, f"El mensaje {mensaje} no se encuentra en {exito}"


@then(u've un mensaje de error "{mensaje}"')
def step_impl(context, mensaje):  # noqa: F811
    # Buscar el elemento que contiene el mensaje de error
    mensaje_error = context.driver.find_element(
        By.CSS_SELECTOR, "ul.errorlist > li")

    # Validar que el texto coincida con el esperado
    assert mensaje_error.text == mensaje


@then(u've un mensaje de error en el correo "{mensaje}"')
def step_impl(context, mensaje):  # noqa: F811
    error = context.driver.find_element(
        By.ID, 'id_correo').get_attribute("validationMessage")

    # Normalizamos las comillas en ambos mensajes
    error_correcto = error.replace("'", '"')
    mensaje_correcto = mensaje.replace("'", '"')

    assert error_correcto == mensaje_correcto
