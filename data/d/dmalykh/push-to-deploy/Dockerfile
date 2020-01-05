FROM sickp/alpine-sshd:latest
MAINTAINER Daniil Malykh <daniil.malykh@gmail.com>

#Install git, sshd, etc...
RUN apk update && apk upgrade
RUN apk update \
    && apk add --no-cache alpine-conf bash tar gzip git ca-certificates 

#Thx https://www.digitalocean.com/community/tutorials/how-to-set-up-automatic-deployment-with-git-with-a-vps

#Create bare repo
RUN mkdir -p /var/repo.git
WORKDIR /var/repo.git
RUN git init --bare

#Write hook
RUN mkdir -p /var/www/
RUN echo -e '#!/bin/sh\ngit --work-tree=/var/www --git-dir=/var/repo.git checkout -f' > hooks/post-receive
RUN chmod +x hooks/post-receive

VOLUME ["/var/www"]

#Set root password. Or you can use other authorization methods, see https://github.com/sickp/docker-alpine-sshd
RUN echo "root:sunshine" | chpasswd

EXPOSE 22