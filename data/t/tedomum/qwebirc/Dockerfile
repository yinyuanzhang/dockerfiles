FROM python:2-alpine

RUN apk add --no-cache build-base python-dev

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt \
 && cp config.py.docker config.py \
 && python compile.py

EXPOSE 9090

ENTRYPOINT ["/app/start.sh"]
