FROM node:dubnium-alpine


RUN npm i -g npm@6.6.0
RUN npm install -g firebase-tools@6.3.1

ARG FILE='linux-x64-64_binding.node'
# install node-sass
RUN \
  mkdir /opt/node-sass/ && \
  wget https://github.com/sass/node-sass/releases/download/v4.11.0/$FILE -O /opt/node-sass/$FILE

ENV SASS_BINARY_PATH=/opt/node-sass/$FILE

USER node

WORKDIR /usr/src/app/

CMD [ "yarn" ]