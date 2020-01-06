FROM node:alpine
MAINTAINER CryoRig "9450688+CryoRig@users.noreply.github.com"

RUN apk --no-cache add --virtual build-dependencies git ca-certificates \
    && apk add --no-cache make gcc g++ python \
    && npm install -g gulp \
    && git clone https://github.com/gskinner/regexr.git /opt/regexr \
    && cd /opt/regexr \
    && npm install gulp-sass \
    && npm audit fix \
    && npm install \
    && apk del build-dependencies

EXPOSE 8080
WORKDIR /opt/regexr
ENTRYPOINT ["gulp","build"]
