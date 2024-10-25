# from behave import given, when, then
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time
#
# @given('que o usuário está na página inicial do Google')
# def step_user_on_google_homepage(context):
#     context.driver.get('https://www.google.com')
#     time.sleep(2)
#
# @when('o usuário buscar por "{query}"')
# def step_user_searches_for(context, query):
#     search_box = context.driver.find_element(By.NAME, 'q')  # Localiza o campo de busca pelo nome
#     search_box.send_keys(query)  # Digita o termo de busca
#     search_box.send_keys(Keys.RETURN)  # Pressiona ENTER para buscar
#
# @then('a página de resultados deve ser exibida')
# def step_search_results_displayed(context):
#     time.sleep(6)  # Aguarda alguns segundos para carregar os resultados
#     assert 'search' in context.driver.current_url  # Verifica se a URL contém "search", o que indica que estamos na página de resultados
#
# @then('os resultados devem conter "{keyword}"')
# def step_results_contain_keyword(context, keyword):
#     results = context.driver.find_elements(By.CSS_SELECTOR, 'h3')  # Seleciona os títulos dos resultados
#     assert any(keyword in result.text for result in results), f'Nenhum resultado contém "{keyword}"'
