# Projeto de testes no Advantage Online Shopping

Este projeto visa validar o fluxo de checkout do site [Advantage Online Shopping](https://advantageonlineshopping.com/#/). Ele foi escrito em Python, utiliza Behave para o BDD, além do Playwright para interagir com o navegador.  
O projeto [utiliza o uv como gerenciador de dependências](https://github.com/astral-sh/uv), ao invés do pip, por ser mais moderno e com várias vantagens. Além de ser mais rápido, ele faz o gerenciamento de dependências de forma determinística, o que garante uma melhor reprodutibilidade dos ambientes.  
Durante a execução o projeto primeiramente faz um healthcheck em todos os endpoints utilizados. Depois ele cria dois novos usuários, um do tipo Admin e outro User, utilizando dados aleatórios gerados pela biblioteca Faker. Após a execução os usuários são apagados.

## Requisitos
- [Python 3.8+](https://www.python.org/downloads)
- [uv](https://github.com/astral-sh/uv)

## Como preparar o ambiente e executar

```bash
uv venv .venv
source .venv/bin/activate
uv sync
playwright install
behave