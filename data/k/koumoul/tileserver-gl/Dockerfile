FROM node:6-stretch
MAINTAINER Petr Sloup <petr.sloup@klokantech.com>

ENV NODE_ENV="production"
VOLUME /data
WORKDIR /data
EXPOSE 80
ENTRYPOINT ["/bin/bash", "/usr/src/app/run.sh"]

RUN apt-get -qq update \
&& DEBIAN_FRONTEND=noninteractive apt-get -y install \
    apt-transport-https \
    curl \
    unzip \
    build-essential \
    python \
    libcairo2-dev \
    libgles2-mesa-dev \
    libgbm-dev \
    libllvm3.9 \
    libprotobuf-dev \
    libxxf86vm-dev \
    xvfb \
&& apt-get clean

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY package.json .
RUN npm install --production
COPY / .
