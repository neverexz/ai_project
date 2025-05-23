FROM --platform=linux/amd64 python:3.12-slim AS base

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        libgl1                    \ 
        libglib2.0-0              \
    && rm -rf /var/lib/apt/lists/*


WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=django:django . .

CMD ["python", "mysite/manage.py", "runserver"]