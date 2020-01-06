FROM node:7.9.0
LABEL version="1.0.0" name="Gravada"

RUN groupadd -r application && useradd -r -g application application
ENV HOME=/home/application

COPY package.json yarn.lock $HOME/gameplan/
RUN chown -R application:application $HOME/* && chown -R application:application $HOME/*

RUN /bin/su application
WORKDIR $HOME/gameplan
RUN npm i -g phantomjs gulp nodemon@latest
# https://github.com/yarnpkg/yarn/issues/749#issuecomment-253253608
RUN yarn --pure-lockfile && yarn install

USER root
COPY . $HOME/gameplan
RUN chown -R application:application $HOME/*

EXPOSE 8001
EXPOSE 27017

ARG DEV_ENV=dev
ENV DEV_ENV=${DEV_ENV}
ENTRYPOINT gulp ${DEV_ENV}

