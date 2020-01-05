FROM node:8.12.0-alpine
ARG MONGO_URL=mongo://localhost:27017
ARG REDIS_URL=redis://localhost:6379
ARG CAIPI_GIT=https://github.com/CaipiLabs/Caipi.git
ARG CAIPI_BRANCH=master
ENV mongoUrl=$MONGO_URL
ENV redisUrl=$REDIS_URL
ENV caipiMode=dev
ENV caipiBranch=$CAIPI_BRANCH


RUN mkdir /home/app

RUN apk --no-cache update \
        && apk add --no-cache \
        python \
        make \
        g++ \
        automake \
        autoconf \
        zlib-dev \
        libpng-dev \
        mongodb-tools \
        pngquant \
        optipng \
        bash \
        lcms2-dev \
        imagemagick \
        git

RUN cd /home \
        && git clone $CAIPI_GIT caipi\
        && cd caipi \
        && git checkout $CAIPI_BRANCH \
        && git reset --hard $CAIPI_BRANCH \
        && (rm package-lock.json||echo "no plock")\
        && npm i\
        && npm link

RUN apk del \
        make \
        g++ \
        automake \
        autoconf \
        zlib-dev \
        libpng-dev \
        pngquant \
        optipng \
        bash \
        lcms2-dev

EXPOSE 80:80

CMD ls /home/app/caipi.conf.json \
        && (\
        chmod a+x /home/caipi.local/etc/cli/caipi-docker-container-init.sh \
        && (/home/caipi.local/etc/cli/caipi-docker-container-init.sh||sleep 5) \
        || chmod a+x /home/caipi/etc/cli/caipi-docker-container-init.sh \
            && /home/caipi/etc/cli/caipi-docker-container-init.sh \
        || sleep 5\
        ) || (mkdir /home/app||echo) && cd /home/app && caipi && ash

