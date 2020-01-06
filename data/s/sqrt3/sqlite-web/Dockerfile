FROM python:3.6-slim

RUN pip install sqlite-web

EXPOSE 8080

ENTRYPOINT ["sqlite_web", "-p", "8080", "-H", "0.0.0.0"]
