FROM trion/ng-cli-e2e:7.3.9

RUN apt-get update -y && apt-get install -y git ssh

MAINTAINER Marvin Oßwald "mail@marvinosswald.de"

ARG NG_CLI_VERSION=7.3.9
ARG USER_HOME_DIR="/tmp"
ARG APP_DIR="/app"
ARG USER_ID=0

USER $USER_ID

RUN curl -sL https://deb.nodesource.com/setup_13.x | bash -
RUN apt-get install -y nodejs
