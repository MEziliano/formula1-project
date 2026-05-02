FROM python:3.11-slim

WORKDIR /app

# Instalar dependências necessárias para requests/scraping (ex: libpq se for usar postgres, etc.)
# Por enquanto vamos deixar simples, mas o Arquiteto poderá refatorar!
RUN apt-get update && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml . 
# Exemplo usando pip, ou pip install . se tiver um setup.py
# Pelo pyproject.toml precisaríamos usar pip install . ou alguma ferramenta como uv/poetry

COPY . /app

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
