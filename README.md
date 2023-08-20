# Calculadora Pet Shop 

Esse módulo em python visa calcular qual pet shop envolve menos custos para banhar cachoros grandes e pequenos dada uma data.

## Intruções para execuação

A interface do sistema é do tipo console. Utilize de preferência a versão 3.10 da linguagem python.
No terminal, entre no diretório do projeto e execute (é necessário ter a linguagem instalada e configurada):

```sh
python best_pet_shop_calculator.py
```
Caso seja mais conveniente, utlize ferramentas online como: https://www.onlinegdb.com/

## Exemplo de uso
A seguir está um exemplo de uso do módulo.

```sh
~ python3 best_pet_shop_calculator.py

Entre com as informações: 03/08/2018 3 5
============ Melhor Pet Shop ============
Nome: Meu Canino Feliz | Preço: R$260.00
=========================================
```
## Decisões de projeto

Como se trata de um sistema simples, foi utilizado apenas um arquivo que representa um módulo. Ele contém as classes que das entidades envolta do problema, além de um código procedural (caso ele seja chamado diretamente) que realiza a leitura, tratamento e impressão dos dados.

Um ponto importante considerado foi a utilização de docstrings para a documentação do código. Também foram utilizadas type hints que permitem especificar os tipos esperados.

Para a construção de um código limpo e robusto (levando em consideração a baixa complexidade da regra de negócio), foram aplicados os princípios solid, principalmente o princípio da responsabilidade única, e o DRY ("Don't repeat yourself"). 
