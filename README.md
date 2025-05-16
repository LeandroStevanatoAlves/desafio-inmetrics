# Projeto de testes no Advantage Online Shopping

Este projeto executa testes BDD com Behave e Playwright para validar o fluxo de checkout do site [Advantage Online Shopping](https://advantageonlineshopping.com/#/).

## Requisitos
- Python 3.8+
- [uv](https://github.com/astral-sh/uv)

## Como executar

```bash
uv venv .venv
source .venv/bin/activate
uv pip install -r pyproject.toml
playwright install
behave