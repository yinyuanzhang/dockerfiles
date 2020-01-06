FROM akilli/base

LABEL maintainer="Ayhan Akilli"

ENV GITEA_CUSTOM=/data
ENV GITEA_USER=app
ENV USER=app

RUN apk add --no-cache \
        gitea && \
    rm -rf /var/lib/gitea && \
    app-user && \
    app-chown

COPY s6/ /s6/gitea/
COPY app.ini /data/conf/app.ini
