FROM debian:buster-slim
MAINTAINER Marco Beinbrech <marco@beinbrech.com>

RUN apt-get update && apt-get install -y \
        rsync  \
        openssh-client \
    && rm -rf /var/lib/apt/lists/*
    
RUN mkdir /app
WORKDIR /app
