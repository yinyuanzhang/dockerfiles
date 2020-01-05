FROM node:boron

# Install firebase-tools
RUN npm install -g firebase-tools

# Install deploy tools
RUN apt-get -y update && apt-get -y install git curl wget unzip

# Install hugo
ENV HUGO_VESION 0.47.1
RUN cd /tmp
RUN wget https://github.com/gohugoio/hugo/releases/download/v${HUGO_VESION}/hugo_${HUGO_VESION}_Linux-64bit.tar.gz
RUN tar xzvf hugo_${HUGO_VESION}_Linux-64bit.tar.gz
RUN mv hugo /usr/local/bin/hugo
