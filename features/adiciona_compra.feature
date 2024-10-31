Feature: Fluxo do Carrinho de Compras
  Scenario: Usuário adiciona e remove itens do carrinho de compras
    Given Usuário está na página inicial da loja online
    When Usuário adiciona um item ao carrinho de compras
    And Usuário visualiza o carrinho de compras
    Then O item é exibido no carrinho de compras
    When Usuário remove o item do carrinho de compras
    Then O carrinho de compras está vazio