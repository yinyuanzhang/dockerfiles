FROM python:3.5.3-alpine

ENV LIBRARY_PATH=/lib:/usr/lib

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN set -x \
      && apk add --update --virtual .build-deps \
              musl-dev \
              gcc \
              tzdata \
      && apk add --virtual .run-deps \
              libjpeg-turbo-dev \
              zlib-dev \
              freetype-dev \
              libpng-dev \
      && pip install --no-cache-dir -r requirements.txt \
      && cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
      && apk del .build-deps \
      && rm -rf /var/cache/apk/*

COPY . /usr/src/app

EXPOSE 5000

CMD ["gunicorn", "-b", ":5000", "-w", "1", "lab:app"]
