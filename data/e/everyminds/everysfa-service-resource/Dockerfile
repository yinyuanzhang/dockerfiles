#########################################################################
# Stage 1 - the build process
#########################################################################
FROM alpine as build-deps

# env
ENV NODE_ENV=production \
    NPM_CONFIG_LOGLEVEL=error \
    NPM_CONFIG_PRODUCTION=true \
    NODE_MODULES_CACHE=false

# install and update: sh, git
RUN echo "$NODE_ENV" && \
    apk add --update --no-cache --repository http://dl-3.alpinelinux.org/alpine/edge/testing \
    git nodejs npm vips-dev fftw-dev gcc g++ make libc6-compat 

# copy code
RUN mkdir /code
WORKDIR /code
COPY package*.json .env.example ./
COPY client ./client
COPY migrations ./migrations
COPY server ./server

# install app
RUN npm install --production \
    && npm dedupe --production \
    && npm install modclean -g \
    && modclean --no-dotfiles --no-progress --run \
    && cd migrations \
    && npm install --production \
    && modclean --no-dotfiles --no-progress --run \
    && cd node_modules \
    && rm -rf `ls | grep -v "everysfa"`

#########################################################################
# Stage 2 - the production environment
#########################################################################
FROM alpine:latest

ARG APPLICATION_PATH=/usr/src/app
ARG USERNAME="app"
ARG USER_ID="1000"
ARG NODE_ENV=production

ENV NODE_ENV="${NODE_ENV}"

WORKDIR ${APPLICATION_PATH}

COPY --from=build-deps /code ${APPLICATION_PATH}

RUN apk update \
    && apk upgrade \
    && apk add --no-cache sqlite nodejs npm \
    && apk add --no-cache --repository https://dl-3.alpinelinux.org/alpine/edge/testing/ vips-dev fftw-dev \
    && npm install -g -s --no-progress pm2@3 \
    && ls -ll \
    && du -hs \
    && npm cache clean --force \
    && apk del npm \
    && rm -rf \
        /usr/share/man/* \
        /usr/includes/* \
        /var/cache/apk/* \
        /root/.npm/* \
        /usr/lib/node_modules/npm/* \
    && adduser -H -D ${USERNAME} -u ${USER_ID} \
    && chown ${USERNAME}:${USERNAME} -R ${APPLICATION_PATH} \
    && deluser --remove-home daemon \
    && deluser --remove-home adm \
    && deluser --remove-home lp \
    && deluser --remove-home sync \
    && deluser --remove-home shutdown \
    && deluser --remove-home halt \
    && deluser --remove-home postmaster \
    && deluser --remove-home cyrus \
    && deluser --remove-home mail \
    && deluser --remove-home news \
    && deluser --remove-home uucp \
    && deluser --remove-home operator \
    && deluser --remove-home man \
    && deluser --remove-home cron \
    && deluser --remove-home ftp \
    && deluser --remove-home sshd \
    && deluser --remove-home at \
    && deluser --remove-home squid \
    && deluser --remove-home xfs \
    && deluser --remove-home games \
    && deluser --remove-home postgres \
    && deluser --remove-home vpopmail \
    && deluser --remove-home ntp \
    && deluser --remove-home smmsp \
    && deluser --remove-home guest

#USER app

# copy init
COPY init.sh /usr/local/bin/
RUN chmod u+x /usr/local/bin/init.sh

HEALTHCHECK --interval=15s --timeout=3s CMD /usr/bin/nc 127.0.0.1 80 < /dev/null || exit 1
EXPOSE 80
ENTRYPOINT ["init.sh"]


