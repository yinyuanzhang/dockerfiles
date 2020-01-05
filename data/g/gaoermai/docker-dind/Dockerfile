FROM docker:18.09.8-dind

ENV DOCKER_HOST 'tcp://docker:2375/'
ENV DOCKER_DRIVER 'overlay2'

RUN apk update && \
    apk add --no-cache --update \
      python3 \
      py3-pip \
      curl \
      jq  && \
    ln -sf /usr/share/zoneinfo/Etc/UTC /etc/localtime && \
    apk add --no-cache --update \
      --virtual .build-deps \
      python3-dev \
      build-base && \
    pip3 install --upgrade pip && \
    pip3 install awscli && \
    apk del --purge -v \
      py3-pip \
      python3-dev \
      build-base && \
    apk del .build-deps && \
    rm /var/cache/apk/*

COPY build_and_push_docker_image.sh /usr/bin/

CMD ["/bin/sh"]
