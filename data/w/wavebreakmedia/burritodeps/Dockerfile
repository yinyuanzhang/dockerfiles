FROM wavebreakmedia/node-ffmpeg

RUN apt-get update && apt-get install -yq --no-install-recommends \
        build-essential \
        expat \
        autoconf \
        bash \
        python \
        libkrb5-dev \
        graphicsmagick \
        libcairo2-dev \
        imagemagick \
        libicu-dev \
        libjpeg-dev \
        libpng-dev \
        libgif-dev \
        libghc-pango-dev \
        netcat-openbsd \
        libkaya-gd-dev \
        git && \
    npm install pm2 -g

ENV HOME=/home/app

RUN mkdir -p $HOME/burrito
COPY package.json $HOME/burrito

WORKDIR $HOME/burrito
RUN npm install --only=prod

