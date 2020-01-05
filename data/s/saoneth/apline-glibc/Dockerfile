FROM alpine:latest

ENV LANG=C.UTF-8
RUN { \
  apk add --no-cache --virtual=.build-dependencies curl ca-certificates wget jq; \
  curl 'https://raw.githubusercontent.com/sgerrand/alpine-pkg-glibc/master/sgerrand.rsa.pub' -o /etc/apk/keys/sgerrand.rsa.pub; \
  curl 'https://api.github.com/repos/sgerrand/alpine-pkg-glibc/releases' \
  | jq '.[0].assets | map(select( .name | contains(".apk") )) | map(select( .name | contains("-dev") | not )) | .[].browser_download_url' \
  | xargs wget --content-disposition;   apk add --no-cache glibc-*.apk; \
  \
  rm "/etc/apk/keys/sgerrand.rsa.pub"; \
  /usr/glibc-compat/bin/localedef --force --inputfile POSIX --charmap UTF-8 "$LANG" || true; \
  echo "export LANG=$LANG" > /etc/profile.d/locale.sh; \
  \
  apk del glibc-i18n; \
  \
  rm "/root/.wget-hsts"; \
  apk del .build-dependencies; \
  rm glibc-*.apk; \
}
