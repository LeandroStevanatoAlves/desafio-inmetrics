# Test Automation Project for Advantage Online Shopping

This project aims to validate the **checkout flow** of the [Advantage Online Shopping](https://advantageonlineshopping.com/#/) website. It was developed using **Python**, uses **Behave for BDD**, and **Playwright** for browser automation. The project is structured with a focus on readability, maintainability, and reproducibility.

It uses [uv](https://github.com/astral-sh/uv) as the dependency manager instead of **pip**, offering a faster and deterministic alternative that ensures consistent environments across developers and CI pipelines.

During test execution, the project first performs a **healthcheck** on all required endpoints. It then creates two users — one **Admin** and one **regular User** — using randomly generated data from the **Faker** library. After the tests finish, both users are automatically removed to keep the environment clean.

## Technologies Used

- [Python 3.8+](https://www.python.org/downloads) — Programming language
- [Behave](https://github.com/behave/behave) — Behavior-Driven Development (BDD) framework
- [Playwright](https://playwright.dev/python/) — End-to-end testing automation tool
- [uv](https://github.com/astral-sh/uv) — Modern Python package manager
- [Faker](https://pypi.org/project/Faker/) — Fake data generator for user creation
- [GitHub Actions](https://github.com/features/actions) — CI/CD pipeline for automated execution

## Continuous Integration

This project is integrated with **GitHub Actions**, ensuring automatic test execution on every push and pull request. After each pipeline run, an execution report is generated with a full summary of the test execution.

## Requirements

- [Python 3.8+](https://www.python.org/downloads)
- [uv](https://github.com/astral-sh/uv)
- [Playwright](https://playwright.dev/python/)

## Setup and Test Execution

```bash
uv venv .venv
source .venv/bin/activate
uv sync
playwright install
behave
```