import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from behave import given, when, then
import time

from behave import use_step_matcher

use_step_matcher("re")

@given("Usuário está na página inicial da loja online")
def user_is_on_the_online_store_homepage(context):
    context.driver.get("https://www.demoblaze.com")
    time.sleep(3)

@when("Usuário adiciona um item ao carrinho de compras")
def user_adds_an_item_to_the_shopping_cart(context):
    item = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//img[@src='imgs/galaxy_s6.jpg']/ancestor::a")))
    item.click()
    add_to_cart_button = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Add to cart']")))
    add_to_cart_button.click()
    WebDriverWait(context.driver, 10).until(EC.alert_is_present())
    Alert(context.driver).accept()

@when("Usuário visualiza o carrinho de compras")
def user_views_the_shopping_cart(context):
    cart_link = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.ID, "cartur")))
    cart_link.click()

@then("O item é exibido no carrinho de compras")
def the_item_is_displayed_in_the_shopping_cart(context):
    item_displayed = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//td[text()='Samsung galaxy s6']")))
    assert item_displayed is not None

@when("Usuário remove o item do carrinho de compras")
def user_removes_the_item_from_the_shopping_cart(context):
    delete_button = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Delete']")))
    delete_button.click()

@then("O carrinho de compras está vazio")
def the_shopping_cart_is_empty(context):
    cart_empty = WebDriverWait(context.driver, 10).until(EC.invisibility_of_element_located((By.XPATH, "//td[text()='Samsung galaxy s6']")))
    assert cart_empty

def before_scenario(context, scenario):
    if "Fluxo do Carrinho de Compras" in scenario.feature.name:
        context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        context.driver.get("https://www.demoblaze.com")
        time.sleep(3)

def after_scenario(context, scenario):
    if hasattr(context, 'driver'):
        context.driver.quit()
