FROM python:3-alpine

ADD ./requirements.txt /tmp

RUN apk --update add --virtual deps gcc musl-dev && \
    pip3 install --no-cache-dir -r /tmp/requirements.txt && \
    apk del deps && \
    rm /tmp/requirements.txt

ADD . /usr/src/app

WORKDIR /usr/src/app

EXPOSE 4222

ENTRYPOINT ["/usr/src/app/docker-entrypoint.sh"]
CMD python3 server.py
