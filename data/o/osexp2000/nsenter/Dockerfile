FROM scratch

# https://github.com/auto-build-docker-images/util-linux-static/blob/master/Dockerfile
COPY --from=osexp2000/util-linux-static /usr/bin/nsenter /

ENV SHELL=/bin/sh

ENTRYPOINT ["/nsenter"]
