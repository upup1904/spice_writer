FROM python:3.8.2-slim-buster

RUN apt-get update && \
    apt-get install -y build-essential python uwsgi

RUN pip install 'django==3.0.5' 'uwsgi==2.0.18' && \
    pip install psycopg2-binary

WORKDIR /website

COPY manage.py .
COPY ./liner_note/ ./liner_note/
COPY ./spice/ ./spice/
