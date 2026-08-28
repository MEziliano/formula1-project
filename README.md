f1-data-project/
│
├── .git/                          # Controle de versão
├── .github/                       # CI/CD (opcional mas recomendado)
│   └── workflows/
│       └── scraper.yml            # Agendamento semanal do scraping
│
├── app/                           # 🔥 CORE DA APLICAÇÃO
│   ├── __init__.py
│   ├── main.py                    # Entry point da FastAPI
│   │
│   ├── api/                       # 🌐 Endpoints REST
│   │   ├── __init__.py
│   │   ├── deps.py                # Dependências do FastAPI (get_db, etc)
│   │   └── v1/
│   │       ├── __init__.py
│   │       ├── router.py          # Agregador de rotas
│   │       ├── races.py           # /races endpoints
│   │       ├── drivers.py         # /drivers endpoints
│   │       └── teams.py           # /teams endpoints
│   │
│   ├── db/                        # 🗄️ Conexão e sessões
│   │   ├── __init__.py
│   │   ├── database.py            # Engine + SessionLocal
│   │   ├── base.py                # Base declarativa do SQLAlchemy
│   │   └── init_db.py             # Script para criar tabelas
│   │
│   ├── models/                    # 📊 Modelos SQLAlchemy + Pydantic
│   │   ├── __init__.py
│   │   ├── orm/                   # Tabelas do banco (SQLAlchemy)
│   │   │   ├── __init__.py
│   │   │   ├── race.py
│   │   │   ├── driver.py
│   │   │   └── team.py
│   │   └── schemas/               # Validação de entrada/saída (Pydantic)
│   │       ├── __init__.py
│   │       ├── race.py
│   │       ├── driver.py
│   │       └── team.py
│   │
│   ├── scraper/                   # 🕷️ Web Scraping
│   │   ├── __init__.py
│   │   ├── client.py              # HTTP client (requests com retry)
│   │   ├── parser.py              # Parse HTML → Pydantic schemas
│   │   ├── runners/               # Executores por tipo de dado
│   │   │   ├── __init__.py
│   │   │   ├── races.py           # Scrape de resultados de corridas
│   │   │   ├── drivers.py         # Scrape de pilotos
│   │   │   └── teams.py           # Scrape de equipes
│   │   └── utils.py               # Helpers (parse_driver, clean_laps)
│   │
│   ├── services/                  # 💼 Lógica de negócio (camada intermediária)
│   │   ├── __init__.py
│   │   ├── race_service.py        # orquestra: scrape → validate → upsert
│   │   ├── driver_service.py
│   │   └── team_service.py
│   │
│   └── config/                    # ⚙️ Configurações
│       ├── __init__.py
│       ├── settings.py            # Pydantic Settings (env vars)
│       └── constants.py           # URLs do site, timeouts, etc
│
├── scripts/                       # 🛠️ Scripts ad-hoc e utilitários
│   ├── seed_db.py                 # Popular DB com dados iniciais
│   ├── full_scrape.py             # Executa scraping completo
│   └── export_csv.py              # Exportar DB para CSV
│
├── tests/                         # 🧪 Testes
│   ├── __init__.py
│   ├── conftest.py                # Fixtures pytest (DB de teste, etc)
│   ├── unit/                      # Testes unitários
│   │   ├── test_parser.py
│   │   └── test_services.py
│   ├── integration/               # Testes de integração
│   │   └── test_api.py
│   └── scraper/                   # Testes do scraping (com HTML fixtures)
│       └── fixtures/
│           └── sample_race_page.html
│
├── alembic/                       # 📜 Migrações de banco (essencial!)
│   ├── versions/
│   ├── env.py
│   └── script.py.mako
├── alembic.ini
│
├── docs/                          # 📚 Documentação
│   ├── architecture.md
│   └── api.md
│
├── docker-compose.yml             # 🐳 Orquestração local
├── Dockerfile                     # 📦 Build da API
├── pyproject.toml                 # 📋 Dependências (uv)
├── uv.lock                        # 🔒 Lock file
├── .env.example                   # 📝 Template de env vars
├── .gitignore
└── README.md