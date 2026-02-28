# Base image z Pythonem
FROM python:3.11-slim

# Katalog roboczy w kontenerze
WORKDIR /app

# instalacja aiohttp
RUN pip install aiohttp

# Kopiuj plik zadania
COPY tasks/task3.py .

EXPOSE 8000

# Komenda startowa
CMD ["python", "task3.py"]