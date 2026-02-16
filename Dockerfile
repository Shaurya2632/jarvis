FROM python:3.13.12

WORKDIR /app

COPY . .

RUN pip install uv

RUN uv sync

CMD ["uv", "run", "main.py"]