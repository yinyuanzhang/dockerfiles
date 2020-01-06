FROM docker

ENV SLEEP_TIME='5m'

RUN apk add --update --no-cache bash curl bind-tools coreutils

COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
