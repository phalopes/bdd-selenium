from behave import *
from selenium import webdriver
import time

from selenium.webdriver.common.by import By


USUARIO = ""
SENHA = ""


@given('we access login screen')
def step_impl(context):
    context.browser = webdriver.Chrome('features/resources/chromedriver')
    context.browser.get('http://localhost:8000/admin')
    time.sleep(3)


@when('inform incorrect user and password')
def step_impl(context):
    form = context.browser.find_element(value='login-form')
    context.browser.find_element(value='id_username').send_keys("usuario")
    context.browser.find_element(value='id_password').send_keys("senha")
    time.sleep(3)
    form.submit()
    time.sleep(3)


@then('system inform invalid credentials')
def step_impl(context):
    assert context.browser.find_element(
        by="class name",
        value='errornote').text.strip() == 'Please enter the correct username and password for a staff account. Note that both fields may be case-sensitive.'
    context.browser.quit()


@when('inform correct user and password')
def step_impl(context):
    form = context.browser.find_element(value='login-form')
    context.browser.find_element(value='id_username').send_keys(USUARIO)
    context.browser.find_element(value='id_password').send_keys(SENHA)
    time.sleep(3)
    form.submit()
    time.sleep(3)


@then('access is granted')
def step_impl(context):
    assert "Django administration" in context.browser.find_element(by="id", value='site-name').text
    assert "Site administration" in context.browser.find_element(by="id", value='content').text
    context.browser.quit()


@Given('we access function to add new question')
def step_impl(context):
    model = context.browser.find_element(By.CLASS_NAME, value='model-question')
    model.find_element(By.CLASS_NAME, value='addlink').click()
    time.sleep(3)


@When('inform correct data')
def step_impl(context):
    form = context.browser.find_element(by="id", value='question_form')
    context.browser.find_element(value='id_question_text').send_keys("What is your age?")
    context.browser.find_element(value='id_pub_date_0').send_keys("2022-08-10")
    context.browser.find_element(value='id_pub_date_1').send_keys("03:58:34")
    time.sleep(3)
    form.submit()
    time.sleep(3)


@then('system answer with data registered successful')
def step_impl(context):
    assert "The question" in context.browser.find_element(by="class name", value='success').text
    assert "was added successfully." in context.browser.find_element(by="class name", value='success').text
    context.browser.quit()
