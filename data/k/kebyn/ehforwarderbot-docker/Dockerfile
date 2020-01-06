FROM python:alpine
MAINTAINER kebyn <kebyn@sina.com>

ENV LANG C.UTF-8
ENV TZ Asia/Shanghai

RUN set -ex \
   && apk --no-cache add \
      python3-dev \
      py3-pillow \
      py3-ruamel.yaml \
      libmagic \
      ffmpeg \
      git \
      gcc \
      zlib-dev \
      jpeg-dev \
      musl-dev \
      libffi-dev \
      openssl-dev \
   && pip3 install git+https://github.com/blueset/ehforwarderbot.git \
   && pip3 install git+https://github.com/blueset/efb-telegram-master.git \
   && pip3 install git+https://github.com/blueset/efb-wechat-slave.git \
   && mkdir -p /root/.ehforwarderbot/profiles/default/blueset.telegram

COPY config.yaml /root/.ehforwarderbot/profiles/default/

VOLUME /root/.ehforwarderbot/profiles/default/blueset.telegram

ENTRYPOINT ["ehforwarderbot"]