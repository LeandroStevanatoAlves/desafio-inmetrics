# Projeto de testes no Advantage Online Shopping

Este projeto executa testes BDD com Behave e Playwright para validar o fluxo de checkout do site [Advantage Online Shopping](https://advantageonlineshopping.com/#/).  
O projeto utiliza o uv ao invés do pip, por ser um gerenciador de pacotes para Python moderno e com várias vantaegns. Além de ser mais rápido, ele faz o gerenciamento de dependências de forma determinística, o que garante uma melhor reprodutibilidade dos ambientes.

## Requisitos
- Python 3.8+
- [uv](https://github.com/astral-sh/uv)

## Como preparar o ambiente e executar

```bash
uv venv .venv
source .venv/bin/activate
uv pip install -r pyproject.toml
playwright install
behave