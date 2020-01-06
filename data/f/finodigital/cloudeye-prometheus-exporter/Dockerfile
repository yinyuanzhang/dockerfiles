FROM python:2.7-alpine

COPY ./app /app

RUN apk add --update --no-cache openssl
RUN pip install -r /app/requirements.txt

EXPOSE 8000

ENV REFRESH_TIME 300
ENV LOG_LEVEL INFO

ENTRYPOINT ["python", "/app/main.py"]

