FROM alpine:3.8 as downloader

ENV  EMBULK_VERSION 0.9.9
RUN  apk add --update --no-cache curl                                                  \
         && curl -o /usr/bin/embulk                                                    \
                 -L "https://dl.bintray.com/embulk/maven/embulk-${EMBULK_VERSION}.jar" \
         && apk -v --purge del curl

FROM java:8-jdk-alpine
COPY --from=downloader /usr/bin/embulk /usr/bin/embulk

ENTRYPOINT ["java", "-jar", "/usr/bin/embulk"]
