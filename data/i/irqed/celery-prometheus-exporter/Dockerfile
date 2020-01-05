FROM python:3.7-alpine

EXPOSE 5050

ENV PYTHONUNBUFFERED 1

WORKDIR /app
ADD . .
RUN pip install .

CMD celery-exporter

