FROM arm32v7/openjdk:8-jre-alpine

COPY qemu-arm-static /usr/bin

ENV USER=jdownloader
ENV UID=500
ENV GROUP=users
ENV GID=100

EXPOSE 5800/tcp
EXPOSE 3129/tcp

RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "$(pwd)" \
    --ingroup "$GROUP" \
    --no-create-home \
    --uid "$UID" \
    "$USER"

RUN apk update && apk upgrade && \
    apk add --no-cache --quiet unrar p7zip tini && \
	mkdir -p /opt/JDownloader

ADD common/entrypoint.sh /opt/JDownloader/entrypoint.sh

RUN chmod +x /opt/JDownloader/entrypoint.sh && \
	chown -R "$UID":"$GID" /opt/JDownloader

USER "$USER"

RUN wget -O /opt/JDownloader/JDownloader.jar --user-agent="https://hub.docker.com/r/jackd0815/jdownloader/" http://installer.jdownloader.org/JDownloader.jar

ENTRYPOINT ["tini", "-g", "--", "/opt/JDownloader/entrypoint.sh"]
