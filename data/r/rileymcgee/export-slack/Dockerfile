FROM python:3.6.5-jessie

WORKDIR /app
COPY app .
RUN pip install -r requirements.txt

COPY docker/entry.sh /usr/local/bin/

ENTRYPOINT ["entry.sh"]