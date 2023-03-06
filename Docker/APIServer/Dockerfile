FROM python:3.11

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY api.py .

CMD uvicorn api:app --host localhost --port 5057