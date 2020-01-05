FROM alpine:edge

#2019*5.2
ENV LANG C.UTF-8

RUN    apk add --update --no-cache ca-certificates  \
        && apk add --no-cache --virtual .run-deps \
                ffmpeg \
                libmagic \
                python3 \
                python3-dev \
                py3-numpy \
                py3-pillow \
                libwebp \
                libffi-dev \
                openssl-dev \
                git \
                py3-yaml \
                py3-requests \
                gcc \
                g++ \
                git
               

RUN set -ex \
        && pip3 install --upgrade pip \
        && pip3 install pyqrcode \
        #&& pip3 install efb-telegram-master==2.0.0b18 \
        #&& pip3 install efb-wechat-slave==2.0.0a17 \
        #&& pip3 install ehforwarderbot==2.0.0b14 \
        #&& pip3 install python-telegram-bot==11.1.0 \
        && pip3 install efb-telegram-master \
        && pip3 install efb-wechat-slave \
        && pip3 install ehforwarderbot \
        && pip3 install python-telegram-bot==11.1.0 \
        && pip3 install --upgrade git+https://github.com/littlecodersh/ItChat.git

CMD ["ehforwarderbot"]
