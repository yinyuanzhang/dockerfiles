FROM jefersonwdc/sdk:1.0

LABEL maintainer="jeferson.wc@outlook.com"

RUN apt-get update -qq && \
    apt-get install nodejs build-essential npm git -y && \
    npm install cordova@9.0.0 ionic npx npm -g && \
    apt-get clean
