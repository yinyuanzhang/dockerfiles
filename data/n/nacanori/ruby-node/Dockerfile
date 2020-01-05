FROM ruby:2.6
LABEL maintainer "nacanori@gmail.com"


RUN mkdir -p $HOME/.ssh

WORKDIR /usr/src/app

ENV NVM_DIR /usr/local/nvm
ENV NVM_VERSION v0.35.1
ENV NODE_VERSION 12.13.1
ENV YARN_VERSION 1.21.1

RUN apt-get update -qq

# for development
RUN apt-get install -y vim git curl build-essential

# for nokogiri
RUN apt-get install -y libxml2-dev libxslt1-dev

# for capybara-webkit
RUN apt-get install -y qt5-default libqt5webkit5-dev gstreamer1.0-plugins-base gstreamer1.0-tools gstreamer1.0-x xvfb  libqt4-dev

# for a JS runtime
RUN apt-get install -y nodejs
RUN mkdir $NVM_DIR
RUN curl https://raw.githubusercontent.com/creationix/nvm/$NVM_VERSION/install.sh | bash \
    && . $NVM_DIR/nvm.sh \
    && nvm install $NODE_VERSION \
    && nvm alias default $NODE_VERSION \
    && nvm use default \
    && npm install --global yarn@$YARN_VERSION

CMD ["/bin/bash"]
