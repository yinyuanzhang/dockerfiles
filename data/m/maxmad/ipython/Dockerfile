FROM python:3.7.1-alpine3.8

WORKDIR /usr/src/app

RUN apk --no-cache add --virtual build-deps gcc musl-dev python3-dev \
    && pip install --no-cache-dir -U ipython \
    && apk del build-deps

COPY entrypoint.sh /

ENTRYPOINT ["sh", "/entrypoint.sh"]

CMD ["ipython"]
