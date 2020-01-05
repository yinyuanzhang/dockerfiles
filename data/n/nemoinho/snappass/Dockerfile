FROM python:3-alpine3.9

EXPOSE 5000

ENV REDIS_HOST=redis
ENV REDIS_PORT=6379
ENV SNAPPASS_REDIS_DB=0

CMD ["snappass"]

RUN cd /tmp \
 && wget https://github.com/pinterest/snappass/archive/master.zip \
 && unzip master.zip \
 && cd snappass-master \
 && apk add gcc libffi-dev libc-dev openssl-dev \
 && python setup.py install \
 && apk del gcc libffi-dev libc-dev openssl-dev \
 && rm -rf /tmp/*

USER nobody
