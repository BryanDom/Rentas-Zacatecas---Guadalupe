from behave import when, given, then
from selenium.webdriver.common.by import By  # importar clase by
import time


@given(u'presiona el botón de Detalles')
def step_impl(context):  # noqa: F811
    context.driver.find_element(By.ID, "btn_detalles").click()


@given(u'da clic en el botón de Interesados')
def step_impl(context):  # noqa: F811
    time.sleep(1)
    (context.driver
     .find_element(
         By.PARTIAL_LINK_TEXT,
         "Interesados").click())


@when(u'presiona el botón de Ver Perfil de algún interesado')
def step_impl(context):  # noqa: F811
    context.driver.find_element(
        By.XPATH, "/html/body/div/div[2]/div/div[2]/div[1]/div[3]/a").click()


@then(u'puede ver la información del interesado seleccionado')
def step_impl(context):  # noqa: F811
    context.driver.find_element(
        By.XPATH, "/html/body/div/div[2]/div/div/div/div[2]/div/a/h5")


@when(u'presiona el botón de Ver Perfil del interesado "{interesado}"')
def step_impl(context, interesado):  # noqa: F811
    view_profile_button = context.driver.find_element(
        By.ID, f"ver_perfil_{interesado}")
    view_profile_button.click()


@then(u'puede ver la información del interesado con ID "{id_interesado}"')
def step_impl(context, id_interesado):  # noqa: F811
    interested_info_element = context.driver.find_element(
        By.XPATH, "/html/body/div/div[2]/div/div/div/div[2]/div/a/h5")
    assert interested_info_element.is_displayed(
    ), f"La información del interesado con ID {id_interesado} " \
       f"no se muestra correctamente"
    time.sleep(1)
