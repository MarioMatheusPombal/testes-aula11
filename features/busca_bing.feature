  # language: pt
  Funcionalidade: Busca no Bing
  Como usuário
  Quero realizar uma busca no Bing
  Para que eu possa ver os resultados da pesquisa

  Cenário: Buscar por "inteligência artificial"
  Dado que o usuário está na página inicial do Bing
  Quando o usuário buscar por "inteligência artificial"
  Então a página de resultados deve ser exibida
  E os resultados devem conter "inteligência artificial"
