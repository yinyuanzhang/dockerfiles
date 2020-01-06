#########################################################################
# Stage 1 - the build process
#########################################################################
FROM alpine:latest as build-deps

# arg
ARG NODE_ENV=production

# env
ENV NODE_ENV="${NODE_ENV}"
ENV NPM_CONFIG_LOGLEVEL warn

# install and update: sh, git
RUN echo "$NODE_ENV" && \
    apk add --no-cache git nodejs npm

# copy code
RUN mkdir /code
WORKDIR /code
COPY package*.json .env.example ./
COPY client ./client
COPY migrations ./migrations
COPY server ./server

# install app
RUN npm install --production && \
    npm dedupe --production && \
    npm install modclean -g && \
    modclean --no-dotfiles --no-progress --run && \
    cd migrations && \
    npm install --production && \
    modclean --no-dotfiles --no-progress --run

#########################################################################
# Stage 2 - the production environment
#########################################################################
FROM alpine:latest

ARG APPLICATION_PATH=/usr/src/app
ENV APK_ADD="sqlite nodejs npm" \
    APK_DEL="npm" \
    USERNAME="app" \
    USER_ID="1000"

WORKDIR ${APPLICATION_PATH}

COPY --from=build-deps /code ${APPLICATION_PATH}

RUN apk update \
    && apk upgrade \
    && apk add --no-cache ${APK_ADD} \
    && npm install -g -s --no-progress pm2@3 \
    #&& ls -ll \
    #&& du -hs \
    && npm cache clean --force \
    && apk del ${APK_DEL} \
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
