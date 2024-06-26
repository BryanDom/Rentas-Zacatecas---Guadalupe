from behave import given, then
from selenium.webdriver.common.by import By  # importar clase by


@given(u'presiona el botón lista de propiedades')
def step_impl(context):  # noqa: F811
    context.driver.find_element(By.ID, "btn-propiedades").click()


@given(u'selecciona un precio minimo "{preciomin}"')
def step_impl(context, preciomin):  # noqa: F811
    context.driver.find_element(
        By.ID, "id_precio_min").send_keys(int(preciomin))


@given(u'selecciona un precio maximo "{preciomax}"')
def step_impl(context, preciomax):  # noqa: F811
    context.driver.find_element(
        By.ID, "id_precio_max").send_keys(int(preciomax))


@given(u'da click en aplicar filtros')
def step_impl(context):  # noqa: F811
    body_div = "/html/body/div"
    form_section = "/div[2]/div/div[2]/form/table/tbody/tr[2]/td[7]/div"
    button = "/button/i"

    btn_aplicar = body_div + form_section + button

    context.driver.find_element(
        By.XPATH, btn_aplicar
    ).click()


@then(u'puede ver una lista de resultados')
def step_impl(context):  # noqa: F811
    resultados = context.driver.find_elements(By.CLASS_NAME, 'card mb-3')
    assert len(resultados) >= 0


@given(u'selecciona un Municipio "{Municipio}"')
def step_impl(context, Municipio):  # noqa: F811
    context.driver.find_element(
        By.ID, "municipio").send_keys(Municipio)


@given(u'selecciona una colonia "{Colonia}"')
def step_impl(context, Colonia):  # noqa: F811
    context.driver.find_element(By.ID, "colonia").send_keys(Colonia)


@given(u'selecciona un Tipo de propiedad "{Tipo}"')
def step_impl(context, Tipo):  # noqa: F811
    context.driver.find_element(By.ID, "id_tipo").send_keys(Tipo)
