FROM python:3.11

# Copy the whole project files in the user app dir
COPY . /usr/src/app

WORKDIR /usr/src/app

RUN pip install --no-cache-dir -r requirements.txt

CMD uvicorn api:app --host 0.0.0.0 --port 5057