FROM node:12-alpine

LABEL description="Alpine based docker container to run MagicMirror in server only mode"
LABEL maintainer="jolegape"

ENV NODE_ENV production
ENV MM_PORT 8080

WORKDIR /opt/magic_mirror

RUN apk add --no-cache git

RUN git clone --depth 1 -b master https://github.com/MichMich/MagicMirror.git .

RUN cp -R modules /opt/default_modules
RUN cp -R config /opt/default_config
RUN npm install --unsafe-perm --silent && npm audit fix

COPY mm-docker-config.js docker-entrypoint.sh /opt/magic_mirror/

RUN chmod +x /opt/magic_mirror/docker-entrypoint.sh

EXPOSE $MM_PORT
CMD ["node", "serveronly"]
ENTRYPOINT ["/opt/magic_mirror/docker-entrypoint.sh"]