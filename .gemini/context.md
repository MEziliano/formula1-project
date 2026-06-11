contexto.md # O "Diário de Bordo" (Decisões de Arquitetura)

Stack Atual: Python 3.11-slim (com uv), FastAPI, Docker.

Decisão Crítica (2026-06): Adotamos o uv dentro do Docker copiando o binário oficial para acelerar builds, e estruturamos as dependências via pyproject.toml.

Decisão Crítica (2026-06): Configuração do Docker Compose Watch (develop: watch) no serviço api para sincronizar código local e rebuilds automáticos.

Infraestrutura: Foco em arquitetura local (Docker e Ollama).

Objetivo: Elaborar um MVP para um site sobre curiosidades sobre a fórmula 1. 
