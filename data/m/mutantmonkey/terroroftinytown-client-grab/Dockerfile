FROM python:3-alpine3.8

RUN apk add --no-cache git \
    && adduser -D -u 1000 grabber \
    && pip install --no-cache-dir seesaw requests

USER grabber
WORKDIR /home/grabber/

COPY --chown=1000 . /home/grabber/

CMD ["run-pipeline3", "pipeline.py", "--concurrent", "6", "--disable-web-server", "mutantmonkey"]
