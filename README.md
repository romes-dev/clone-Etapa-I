# Controle de Gastos Pessoais

![CI](https://github.com/romes-dev/clone-Etapa-I/actions/workflows/ci.yml/badge.svg)

**Acesse a aplicação:** [link-do-deploy-aqui](#) *(atualizar após o deploy no Railway)*

## Descrição do Problema

Muitas pessoas têm dificuldade em acompanhar para onde vai o seu dinheiro ao longo do mês. Sem um registro organizado, gastos com alimentação, transporte e lazer passam despercebidos, dificultando o planejamento financeiro pessoal.

## Proposta de Solução

Aplicação web que permite registrar, categorizar e visualizar despesas pessoais de forma simples. Exibe um resumo por categoria, o total gasto no mês e as cotações atuais do dólar e euro para referência.

## Público-alvo

Pessoas que desejam controlar seus gastos pessoais e ter uma visão clara de suas finanças mensais.

## Funcionalidades

- Listar todas as despesas com filtro por categoria
- Adicionar novas despesas com descrição, valor, categoria e data
- Editar despesas existentes
- Excluir despesas
- Visualizar resumo de gastos por categoria
- Exibir cotações do dólar e euro em tempo real (via AwesomeAPI)

## Tecnologias Utilizadas

- Python 3.13
- Django 4.2
- SQLite
- requests (integração com API externa)
- gunicorn (servidor de produção)
- pytest / pytest-django
- ruff
- GitHub Actions (CI)
- Railway (Deploy)

## Instalação

```bash
# Clone o repositório
git clone https://github.com/romes-dev/clone-Etapa-I.git
cd clone-Etapa-I

# Crie e ative o ambiente virtual
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac

# Instale as dependências
pip install -r requirements.txt

# Execute as migrações
python manage.py migrate

# Inicie o servidor
python manage.py runserver
```

Acesse em: http://127.0.0.1:8000

## Testes

```bash
pytest
```

## Lint

```bash
ruff check .
```

## Versão

1.1.0

## Autor

Romes Heriberto — [github.com/romes-dev](https://github.com/romes-dev)

## Repositório

[github.com/romes-dev/clone-Etapa-I](https://github.com/romes-dev/clone-Etapa-I)
