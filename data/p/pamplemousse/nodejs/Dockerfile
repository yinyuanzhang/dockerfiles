FROM node:10

RUN apt-get update && apt-get install apt-transport-https -y

RUN yarn global add \
      doctoc \
      elm@0.19.0 \
      heroku \
      http-server \
      jsdoc \
      json-server \
      js-yaml \
      livedown \
      prettier \
      standard

USER node

RUN rm -rf ~/.elm
