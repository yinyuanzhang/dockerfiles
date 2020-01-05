FROM alpine:3.8 as downloader

ENV  DIGDAG_VERSION 0.9.31
RUN  apk add --update --no-cache curl                               \
         && curl -o /usr/bin/digdag                                 \
                 -L "https://dl.digdag.io/digdag-${DIGDAG_VERSION}" \
         && apk -v --purge del curl

FROM java:8-jdk-alpine
COPY --from=downloader /usr/bin/digdag /usr/bin/digdag
RUN  chmod 755 /usr/bin/digdag                    \
         && apk -v --update add python            \
                                py-pip            \
                                groff             \
                                less              \
                                mailcap           \
         && pip install --upgrade awscli==1.16.52 \
         && apk -v --purge del py-pip             \
         && rm /var/cache/apk/*

VOLUME /root/.aws

