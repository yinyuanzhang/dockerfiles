FROM lanestolen/base-image
LABEL maintainer="Lanestolen"

ENV VERSION 1

RUN \
    apk add --no-cache \
        python3 && \
        python3 -m ensurepip && \
        python3 -m pip install flexget transmissionrpc && \
        rm -r /root/.cache


COPY root / /

EXPOSE 3539
VOLUME ["/config","/data"]
