FROM node:6-slim

RUN apt update && apt install mysql-client -y \
    && apt-get clean && apt-get autoclean && apt-get autoremove --purge -y \
    && rm -rf /var/cache/apt/* && rm -rf /var/lib/apt/lists/* && rm -rf /tmp/*

RUN echo 'alias ll="ls -alh"' >> ~/.bashrc
ADD lib/wait-for-it.sh /opt/
