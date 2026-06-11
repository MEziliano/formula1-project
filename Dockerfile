FROM python:3.11-slim

# Copia o binário do uv diretamente da imagem oficial do Astral
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

# Instala dependências de sistema necessárias (ex: curl) e limpa o cache do apt
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Configurações de ambiente para o Python e uv
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV UV_COMPILE_BYTECODE=1

# Copia apenas o arquivo de configuração para cachear a camada de dependências
COPY pyproject.toml .

# Instala as dependências listadas no pyproject.toml no ambiente de sistema do container
RUN uv pip install --system -r pyproject.toml

# Copia todo o código da aplicação
COPY . /app

EXPOSE 8000

CMD ["python", "main.py"]