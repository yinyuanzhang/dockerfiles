# Inherits from: https://hub.docker.com/r/filebrowser/filebrowser
# Original Dockerfile: https://github.com/filebrowser/filebrowser/blob/master/Dockerfile
# Build Docs: https://github.com/filebrowser/community/blob/master/builds.md
FROM filebrowser/filebrowser AS base
FROM alpine:latest AS img
COPY --from=base /filebrowser /usr/bin/filebrowser

RUN apk add --update \
    ca-certificates \
    bash \
    openssl \
    youtube-dl \
    vim \
    bzip2 \
    curl \
    iperf3 \
    mediainfo \
    parallel \
    pigz \
    bind-tools \
    wget \
    bind-tools \
    findutils \
    git \
    imagemagick \
    libbz2 \
    libcurl \
    openssh-client \
    openssh \
    python2 \
    python2-dev \
    python3 \
    python3-dev \
    stunnel \
    aria2 \
    tar \
    unrar \
    zip
    

RUN if [ ! -d "/config" ]; then \
    mkdir -p /config/;\
    fi



# https://github.com/filebrowser/community/blob/master/builds.md
#RUN curl -L $( \
#         curl -s https://api.github.com/repos/filebrowser/filebrowser/releases/latest \
#       | grep "browser_download_url.*linux-amd64.*tar.gz" \
#       | cut -d : -f 2,3 \
#       | tr -d \" \
#     ) -o "/tmp/filebrowser.tar.gz"
     

#RUN cd /tmp &&  tar -xzvf filebrowser.tar.gz

#RUN mv /tmp/filebrowser /usr/bin/filebrowser


EXPOSE 80/tcp

VOLUME /srv
VOLUME /config

ADD        entrypoint.sh /entrypoint.sh

ENTRYPOINT [ "/bin/bash", "-c", "/entrypoint.sh"]
#ENTRYPOINT [ "/usr/bin/filebrowser", "-c", "/config/filebrowser.json", "-d", "/config/filebrowser.db"]
