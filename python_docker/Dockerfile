# ===== STAGE 1: builder =====
FROM python:3.11-slim AS builder

WORKDIR /install

# instalujemy aiohttp do osobnego katalogu
RUN pip install --no-cache-dir --prefix=/install aiohttp

# ===== STAGE 2: runtime =====
FROM python:3.11-slim

WORKDIR /app

# kopiujemy tylko zainstalowane pakiety
COPY --from=builder /install /usr/local

# kopiujemy kod aplikacji
COPY tasks/task3.py .

EXPOSE 8000

CMD ["python", "task3.py"]