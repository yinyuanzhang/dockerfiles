# SYNCTHING
FROM alpine:latest

LABEL maintainer="docker@mbffm.de"
LABEL version="1.0"

# VARIABLES
ENV SYNCTHING_USER syncthing
ENV SYNCTHING_GROUP syncthing
ENV SYNCTHING_UID 22000
ENV SYNCTHING_GID 22000

# CREATE GROUP, USER AND DATA
RUN addgroup -g $SYNCTHING_GID $SYNCTHING_GROUP && \
  adduser -h /data -s /sbin/nologin -G $SYNCTHING_GROUP -D -u $SYNCTHING_UID $SYNCTHING_USER

# CREATE FOLDERS
RUN mkdir \
    /app \
    /config && \
  chown $SYNCTHING_USER \
    /app \
    /config \
    /data && \
  chmod 700 \
    /app \
    /config && \
  chmod 750 \
    data

# INSTALL PACKAGES
RUN apk add --update \
    curl \
    jq && \
  rm -rf /var/cache/apk/*

# INSTALL SYNCTHING
RUN set -x && \
  cd /app && \
  release=${release:-$(curl -s https://api.github.com/repos/syncthing/syncthing/releases/latest | jq -r .tag_name )} && \
  curl -s -L https://github.com/syncthing/syncthing/releases/download/${release}/syncthing-linux-amd64-${release}.tar.gz | tar -zx && \
  mv syncthing-linux-amd64-*/syncthing . && \
  rm -rf syncthing-linux-amd64-*

# CHANGE TO USER
USER $SYNCTHING_USER

# VOLUMES
VOLUME ["/config"]
VOLUME ["/data"]

# PORTS
EXPOSE 8384/TCP
EXPOSE 21027/TCP
EXPOSE 22000/TCP

# ENTRYPOINT
ENTRYPOINT ["/app/syncthing"]
CMD ["-home", "/config", "-gui-address", "0.0.0.0:8384"]
