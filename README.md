f1_project/
├── .gemini/
│ ├── gemini.md # O "Maestro" (Instruções dos Agentes)
│ ├── contexto.yaml # O "Diário de Bordo" (Decisões de Arquitetura)
│ ├── ferramentas.json # Configurações de permissões (Terminal/Web)
│ └── lições_aprendidas.md # O seu "Log Socrático" de aprendizado
├── .geminiignore # Arquivos que a IA deve ignorar
├── app/
│   ├── __init__.py
│   ├── models/          # Modelos Pydantic e SQLAlchemy
│   │   ├── __init__.py
│   │   ├── schemas.py   # Validação Pydantic
│   │   └── tables.py    # Definição das tabelas SQL
│   ├── scraper/         # Scripts de raspagem
│   │   ├── __init__.py
│   │   ├── races.py
│   │   ├── drivers.py
│   │   └── teams.py
│   ├── db/              # Configuração do Banco
│   │   ├── __init__.py
│   │   ├── connection.py
│   │   └── crud.py      # Lógica de INSERT/UPSERT
│   └── utils/           # Utilitários
│       └── logger.py
├── data/                # Dados brutos (CSV)
├── tests/               # Testes unitários
├── .env
├── .gitignore
├── docker-compose.yml
├── requirements.txt
└── main.py