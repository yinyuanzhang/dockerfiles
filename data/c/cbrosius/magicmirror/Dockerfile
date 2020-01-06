FROM node:lts-alpine

RUN apk update && apk upgrade && \
    apk add --update bash git npm

ENV NODE_ENV production
WORKDIR /opt/magic_mirror

RUN git clone https://github.com/MichMich/MagicMirror.git .
RUN cp -R modules /opt/default_modules
RUN cp -R config /opt/default_config
RUN npm install --unsafe-perm --silent

COPY server-only-default-config.js /opt/magic_mirror/config/config.js 
COPY server-only-german-sample-config.js /opt/magic_mirror/config/server-only-german-sample-config.js 
COPY server-only-default-config.js docker-entrypoint.sh ./
RUN chmod +x ./docker-entrypoint.sh

VOLUME [ "/opt/magic_mirror/config", "/opt/magic_mirror/modules" ]

EXPOSE 8080
ENTRYPOINT ["./docker-entrypoint.sh"]
CMD ["node", "serveronly"]
