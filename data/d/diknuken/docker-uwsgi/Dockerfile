FROM python:3.6

RUN pip install uwsgi

WORKDIR /app

RUN pip install --no-cache-dir uwsgi virtualenv

COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

ENTRYPOINT ["/docker-entrypoint.sh"]
