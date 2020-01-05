FROM ubuntu
MAINTAINER rheil@mergeworld.com

RUN apt-get update
RUN apt-get install -y \
    nodejs \ 
    bzip2 \
    build-essential \
    curl \
    rsync \
    ssh
RUN curl -sL https://deb.nodesource.com/setup_11.x | bash -
RUN apt-get install -y nodejs
RUN npm install grunt bower node-sass
