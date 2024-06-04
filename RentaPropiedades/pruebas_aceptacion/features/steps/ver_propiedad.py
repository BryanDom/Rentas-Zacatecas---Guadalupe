from behave import when, then
from selenium.webdriver.common.by import By  # importar clase by


@when(u'presiona el botón de Detalles')
def step_impl(context):  # noqa: F811
    context.driver.find_element(By.ID, "btn_detalles").click()


@then(u'puede ver la información de la propiedad seleccionada')
def step_impl(context):   # noqa: F811
    context.driver.find_element(
        By.XPATH, "/html/body/div/div[2]/div/div/div[2]/h1/strong")
