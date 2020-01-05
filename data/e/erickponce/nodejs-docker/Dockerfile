FROM node:7.10.0
MAINTAINER Erick Ponce Leão "erickponceleao@gmail.com"
ENV APP_VERSION=0.0.2

ADD package.json /install/
WORKDIR /install
# "Installs app default dependencies"
RUN npm config set registry http://registry.npmjs.org/ \
    && npm install --prod

VOLUME /usr/src/app
WORKDIR /usr/src/app/
ADD entrypoint.sh /var/tmp/entrypoint.sh

EXPOSE 8888
ENTRYPOINT ["/var/tmp/entrypoint.sh"]
CMD [ "npm", "start" ]

