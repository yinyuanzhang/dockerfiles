FROM lsiobase/alpine

LABEL maintainer pegasy

RUN apk add --no-cache \
  mariadb-client \
  rsync \
  tar \
  sed \
  bash && \
  rm -rf \
    /tmp/*

ENV \
  DB_HOSTNAME=localhost, \
  DB_USERNAME=nextcloud, \
  DB_PASSWORD=qwerty, \
  DB_DATABASE=nextcloud, \
  MAX_FILES_TO_KEEP=7

VOLUME /data /config /backup

COPY backup.sh .
ENTRYPOINT ["bash", "backup.sh"]
