FROM node:slim

LABEL maintainer="Dragnucs <touhami@touha.me>"

RUN yarn global add \
      @vue/cli \
      @vue/cli-service \
      @vue/cli-plugin-babel \
      @vue/cli-plugin-eslint \
      @vue/cli-plugin-pwa \
      @vue/eslint-config-standard

RUN mkdir /app

WORKDIR /app
