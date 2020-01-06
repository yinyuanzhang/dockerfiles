FROM alpine

RUN apk add --no-cache --update \
    inotify-tools \
    gettext \
    bash

COPY bin/ /

RUN chmod +x /docker-entrypoint

# arg1: /watch_dir arg2: /script_to_execute

ENTRYPOINT ["/docker-entrypoint"]