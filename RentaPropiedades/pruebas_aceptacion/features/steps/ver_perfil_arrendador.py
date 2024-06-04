from behave import then
from selenium.webdriver.common.by import By  # importar clase by


@then(u'puede ver su ocupacion "{ocupacion}"')
def step_impl(context, ocupacion):  # noqa: F811
    oc = context.driver.find_element(
        By.XPATH, '/html/body/div/div[2]/div/div/div/div[2]/div/p[4]').text
    assert ocupacion in oc


@then(u'puede ver sus preferencias de arrrendamiento "{preferencia}"')
def step_impl(context, preferencia):  # noqa: F811
    pr = context.driver.find_element(
        By.XPATH, '/html/body/div/div[2]/div/div/div/div[2]/div/p[6]').text
    assert preferencia in pr
