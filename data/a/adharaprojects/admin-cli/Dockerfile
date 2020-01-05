FROM node:8-alpine

# Set the working directory to /app
WORKDIR /app

# TODO: some of these dependencies are only required at build time (not for running), remove them to keep the image slim
RUN apk update && \
    apk upgrade && \
    apk add bash docker py-pip git libcurl libgit2-dev openssl curl g++ gcc gnupg libgcc make alpine-sdk python openssh-client

# Install docker-compose
RUN pip install docker-compose

# Copy the current directory contents into the container at /app
ADD . /app

RUN ln -s /usr/lib/libcurl.so.4 /usr/lib/libcurl-gnutls.so.4

RUN npm install

RUN echo -e '#!/bin/bash\n/app/bin/run "$@"' > /usr/bin/adhara && \
    chmod +x /usr/bin/adhara
