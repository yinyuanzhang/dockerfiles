FROM node:current-alpine


ENV APP_HOME=/site 
ENV PORT=8000
WORKDIR $APP_HOME

EXPOSE 8000

RUN apk update && \
    apk add --update --repository http://dl-cdn.alpinelinux.org/alpine/edge/community vips-tools vips-dev fftw-dev gcc g++ make libc6-compat nano && \
    apk add git && \
    apk add python && \
    rm -rf /var/cache/apk/*

RUN npm install --global gatsby --no-optional gatsby@1.9 

RUN mkdir -p $APP_HOME

ARG UID=1001
ARG GID=1001

RUN addgroup -g ${GID} abc \
 && adduser -D -u ${UID} -G abc abc \
 && chown -R ${UID}:${GID} ${APP_HOME}/

EXPOSE ${PORT}
VOLUME ["${APP_HOME}/"]

COPY ./entry.sh /
RUN chmod +x /entry.sh

USER abc

ENTRYPOINT ["/entry.sh"]

