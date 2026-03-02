FROM python:3.11-slim

WORKDIR /app

RUN pip install aiohttp asyncpg

COPY tasks/task6.py .

EXPOSE 8000

CMD ["python", "task6.py"]