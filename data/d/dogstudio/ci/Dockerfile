FROM docker:latest
MAINTAINER Dogstudio <developers@dogstudio.be>

RUN apk add --update bash git openssh-client rsync curl pkgconfig autoconf automake libtool nasm build-base zlib-dev
RUN mkdir -p /cache/apk && ln -s /cache/apk /etc/apk/cache
RUN which ssh-agent || ( apk add --update openssh )
RUN eval $(ssh-agent -s)
RUN mkdir -p ~/.ssh && chmod 700 ~/.ssh

#Add Minio client
RUN wget https://dl.min.io/client/mc/release/linux-amd64/mc
RUN chmod +x mc
RUN mv mc /usr/local/bin
