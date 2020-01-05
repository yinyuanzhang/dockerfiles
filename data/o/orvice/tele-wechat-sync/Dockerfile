FROM alpine:edge

WORKDIR /usr/src/app

ENV LANG C.UTF-8

RUN apk add --update --no-cache ca-certificates

RUN set -ex \
        && apk add --no-cache --virtual .run-deps \
                ffmpeg \
                libmagic \
                python3 \
                py3-numpy \
                py3-pillow

COPY requirements.txt ./
COPY config.docker.py ./config.py
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python3", "./main.py" ]
