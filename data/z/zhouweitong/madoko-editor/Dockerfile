FROM node:latest
MAINTAINER xml@live.com
RUN apt-get update && \
    apt-get -y dist-upgrade && \
    apt-get install -y \
        imagemagick \
        inkscape \
        make \
        texlive-full \
        inotify-tools \
        xzdec \
        && apt-get clean
RUN npm install madoko -g && npm install madoko-local -g
RUN tlmgr init-usertree
COPY add_user add_user
RUN ./add_user
USER developer