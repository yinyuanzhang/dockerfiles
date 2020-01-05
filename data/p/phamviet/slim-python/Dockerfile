FROM python:2.7-slim

RUN apt-get update && apt-get install -y --no-install-recommends libmysqlclient-dev gcc

ENV FLASK_APP slim.py

RUN pip install gunicorn flask docker MySQL-python Flask-BasicAuth

RUN apt-get purge -y --auto-remove gcc && rm -rf /var/lib/apt/lists/*

COPY . /app

WORKDIR /app

VOLUME /data

EXPOSE 5000

ENTRYPOINT ["gunicorn"]

CMD ["-w", "4", "-b", "0.0.0.0:5000", "slim:app"]