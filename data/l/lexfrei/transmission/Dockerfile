FROM alpine:edge

EXPOSE 9091 51413/tcp 51413/udp

VOLUME ["/downloads"]
VOLUME ["/var/lib/transmission/.config/transmission-daemon"]

COPY conf/settings.json /var/lib/transmission/.config/transmission-daemon/settings.json

HEALTHCHECK --interval=60s --timeout=15s \
   CMD netstat -lntp | grep -q '0\.0\.0\.0:9091'

RUN ["apk", "upgrade", "--update", "--no-cache", "--no-progress"]
RUN ["apk", "add", "--update", "--no-cache", "--no-progress", "transmission-daemon"]

RUN ["chown", "transmission:transmission", "/downloads"]
RUN ["chown", "transmission:transmission", "/var/lib/transmission/.config/transmission-daemon/settings.json"]

USER transmission

ENTRYPOINT ["/usr/bin/transmission-daemon", "--foreground"]
