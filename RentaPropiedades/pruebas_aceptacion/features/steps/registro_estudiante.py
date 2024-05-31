from behave import when, given, then
from selenium import webdriver
from selenium.webdriver.common.by import By #importar clase by
import time
import os

# Ruta base del proyecto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))


@given(u'que el estudiante ingresa a la url "{url}"')
def step_impl(context, url):
    context.driver = webdriver.Chrome()
    context.driver.get(url)


@given(u'presiona el botón Crear cuenta estudiante')
def step_impl(context):
    time.sleep(1)
    # By.LINK_TEXT requiere que coincida exactamente el texto, 
    # mientras que By.PARTIAL_LINK_TEXT permite coincidencias parciales, 
    # lo cual es más adecuado para este caso dado que el texto completo del 
    # botón incluye cosas extras como la clase.
    context.driver.find_element(By.PARTIAL_LINK_TEXT, "Crear cuenta estudiante").click()

@given(u'presiona el botón Siguiente')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.CLASS_NAME, "btn_siguiente").click()
    
@given(u'presiona el botón Aceptar y continuar')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.ID, "btn-aceptar").click()


@given(u'escribe su nombre "{nombre}", sus apellidos "{apellidos}", su edad "{edad}"')
def step_impl(context, nombre, apellidos, edad):
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
def step_impl(context, sexo):
    time.sleep(1)
    radio_button = context.driver.find_element(By.XPATH, '//input[@value="' + sexo + '"]')
    radio_button.click()

@given(u'selecciona su foto de perfil "{foto}"')
def step_impl(context, foto):
    time.sleep(1)
    ruta_imagen = os.path.join(BASE_DIR, foto.replace("\\", os.sep))
    # Encontrar el elemento de entrada de archivo
    upload_input = context.driver.find_element(By.ID, 'id_foto_perfil')
    
    print(f"Ruta de imagen construida: {ruta_imagen}")  # Imprimir la ruta para depuración
    # Enviar la ruta absoluta al elemento de entrada de archivo
    upload_input.send_keys(ruta_imagen)
    
    # Esperar un momento para que el archivo se cargue
    time.sleep(2)


@given(u'escribe su universidad actual "{universidad}"')
def step_impl(context, universidad):
    unive = context.driver.find_element(By.ID, 'id_universidad_actual')
    unive.clear()
    unive.send_keys(universidad)


@given(u'escribe su teléfono "{telefono}"')
def step_impl(context, telefono):
    tel = context.driver.find_element(By.ID, 'id_telefono')
    tel.clear()
    tel.send_keys(telefono)



@given(u'escribe su WhatsApp "{whatsapp}"')
def step_impl(context, whatsapp):
    whats = context.driver.find_element(By.ID, 'id_whatsapp')
    whats.clear()
    whats.send_keys(whatsapp)


@given(u'escribe su correo "{correo}"')
def step_impl(context, correo):
    corr = context.driver.find_element(By.ID, 'id_correo')
    corr.clear()
    corr.send_keys(correo)


@given(u'escribe sus preferencias de búsqueda "{preferencias}"')
def step_impl(context, preferencias):
    pref = context.driver.find_element(By.ID, 'id_preferencias_busqueda')
    pref.clear()
    pref.send_keys(preferencias)


@given(u'escribe sus pasatiempos "{pasatiempos}"')
def step_impl(context, pasatiempos):
    pasa = context.driver.find_element(By.ID, 'id_pasatiempos')
    pasa.clear()
    pasa.send_keys(pasatiempos)

@given(u'puede ver el mensaje del compromiso del sistema')
def step_impl(context):
    mensaje_compromiso = context.driver.find_element(By.XPATH, '/html/body/div/div/p[2]').text
    compromiso_esperado = (
        "Nuestro compromiso:\n\n"
        "La plataforma de alquiler en Zacatecas y Guadalupe "
        "es una comunidad acogedora donde queremos que todos se "
        "sientan como en casa sin importar su origen. Para garantizar este ambiente inclusivo, "
        "pedimos que todos los usuarios se comprometan a seguir lo siguiente:\n\n"
        "En nuestra comunidad, nos esforzamos por respetar y tratar a todos sin prejuicios, "
        "sin importar el color de piel, la religión, la nacionalidad, la etnia, el género, la identidad de género, "
        "la orientación sexual o si tienen alguna discapacidad. Queremos que todos se sientan bienvenidos y seguros "
        "al utilizar nuestros servicios. Gracias por unirte a nosotros para crear un entorno donde la diversidad es valorada."
    )
    assert mensaje_compromiso == compromiso_esperado, f"El mensaje del compromiso no coincide. Esperado: '{compromiso_esperado}', Encontrado: '{mensaje_compromiso}'"
    

@given(u'ingresa la contraseña "{contrasenia}"')
def step_impl(context, contrasenia):
    context.driver.find_element(By.ID, 'id_password').send_keys(contrasenia)



@given(u'para confirmar nuevamente ingresa la contraseña "{contrasenia}"')
def step_impl(context, contrasenia):
    context.driver.find_element(By.ID, 'id_re_pass').send_keys(contrasenia)

@given(u'no completa el campo de pasatiempos "{campo}"')
def step_impl(context, campo):
    context.driver.find_element(By.ID, 'id_pasatiempos').send_keys(campo)

@when(u'presiona el botón Continuar')
def step_impl(context):
    context.driver.find_element(By.ID, "btn-crearContra").click()
    

@when(u'presiona el botón Siguiente')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.CLASS_NAME, "btn_siguiente").click()


@then(u'puede ver el mensaje "{mensaje}"')
def step_impl(context, mensaje):
    exito = context.driver.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/div/h1').text
    assert mensaje == exito, f"El mensaje {mensaje} no se encuentra en {exito}"
    
@then(u've un mensaje de error "{mensaje}"')
def step_impl(context, mensaje):
    # Buscar el elemento que contiene el mensaje de error
    mensaje_error = context.driver.find_element(By.CSS_SELECTOR, "ul.errorlist > li")

    # Validar que el texto coincida con el esperado
    assert mensaje_error.text == mensaje

@then(u've un mensaje de error en el correo "{mensaje}"')
def step_impl(context, mensaje):
    error = context.driver.find_element(By.ID, 'id_correo').get_attribute("validationMessage")
    
    # Normalizamos las comillas en ambos mensajes
    error_correcto = error.replace("'", '"')
    mensaje_correcto = mensaje.replace("'", '"')
 
    assert error_correcto == mensaje_correcto
    