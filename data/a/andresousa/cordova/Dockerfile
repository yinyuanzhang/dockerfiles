FROM andresousa/androidsdk:release-1.1.2

LABEL maintainer="lucas.eduardo.developer@gmail.com"

RUN apt-get update -qq && \
    apt-get install nodejs build-essential npm git -y && \
    npm install cordova@8.0.0 ionic@2.1.0 gulp-cli@2 gulp@2 -g && \
    apt-get clean