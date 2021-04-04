FROM docker.io/jfloff/alpine-python:3.8
WORKDIR /colors
ENV FLASK_APP colors.py
ENV ENVIRONMENT Production
ENV FILE_NAME colors.json


COPY colors /colors
COPY requirements.txt /colors

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT flask run --host=0.0.0.0