FROM python:3.13.0-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    openssh-client \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN ls -la /app && ls -la /app/src

CMD ["python", "src/main.py"]