FROM python:3.7-slim

RUN pip3 install flask gunicorn

COPY . /app
WORKDIR /app

EXPOSE 80
ENV \
  PYTHONUNBUFFERED=1 \
  GREETING="Greetings!"

CMD ["/app/entrypoint"]
