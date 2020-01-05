FROM ubuntu:14.04

ARG UID=1001
ARG GID=1001

RUN apt-get update && \
apt-get -y upgrade && \
apt-get install -y nodejs npm git && \
npm install -g bower && \
ln -s /usr/bin/nodejs /usr/bin/node

RUN export uid=$UID gid=$GID && \
    mkdir -p /home/developer/project && \
    echo "developer:x:${uid}:${gid}:Developer,,,:/home/developer:/bin/bash" >> /etc/passwd && \
    echo "developer:x:${uid}:" >> /etc/group && \
    echo "developer ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/developer && \
    chmod 0440 /etc/sudoers.d/developer && \
    chown ${uid}:${gid} -R /home/developer

USER developer
ENV HOME /home/developer
WORKDIR /home/developer/project
