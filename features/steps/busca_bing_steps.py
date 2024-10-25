from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


@given('que o usuário está na página inicial do Bing')
def step_user_on_bing_homepage(context):
    context.driver.get('https://www.bing.com/')
    WebDriverWait(context.driver, 100).until(
        EC.presence_of_element_located((By.ID, 'sb_form_q'))
    )


@when('o usuário buscar por "{query}"')
def step_user_searches_for(context, query):
    # Aceitar cookies ou fechar pop-up, se necessário
    try:
        accept_button = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.bnp_btn_accept'))
        )
        accept_button.click()
    except Exception as e:
        print("Botão de aceitar cookies não encontrado ou não clicável.")
        pass  # Se o botão não estiver presente, continue

    searchbox = WebDriverWait(context.driver, 100).until(
        EC.element_to_be_clickable((By.ID, 'sb_form_q'))
    )
    searchbox.clear()
    searchbox.send_keys(query)
    searchbox.send_keys(Keys.RETURN)


@then('a página de resultados deve ser exibida')
def step_search_results_displayed(context):
    try:
        WebDriverWait(context.driver, 100).until(
            EC.url_contains('search?q=')
        )
        WebDriverWait(context.driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'li.b_algo h2'))
        )
    except TimeoutException as e:
        # Captura uma screenshot da página
        screenshot_path = os.path.join(os.getcwd(), 'screenshot.png')
        context.driver.save_screenshot(screenshot_path)
        print(f"Screenshot salva em {screenshot_path}")
        raise e


@then('os resultados devem conter "{keyword}"')
def step_results_contain_keyword(context, keyword):
    results = WebDriverWait(context.driver, 100).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'li.b_algo h2'))
    )
    assert any(keyword.lower() in result.text.lower() for result in results), f'Nenhum resultado contém "{keyword}".'
