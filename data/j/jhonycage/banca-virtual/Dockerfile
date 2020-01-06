FROM circleci/python:3.7.3-browsers

RUN pip3 --version
RUN sudo pip3 install awscli --upgrade
RUN aws --version

RUN curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.34.0/install.sh | bash

ENV NODE_VERSION 8.15.0
ENV NVM_DIR /home/circleci/.nvm
RUN . ~/.nvm/nvm.sh && nvm install $NODE_VERSION && nvm alias default $NODE_VERSION
ENV NODE_PATH $NVM_DIR/v$NODE_VERSION/lib/node_modules
ENV PATH $NVM_DIR/versions/node/v$NODE_VERSION/bin:$PATH

RUN npm install -g ionic@3.9.2 \
    && npm install -g cordova \
    && npm install -g gulp \
    && npm install -g sonarqube-scanner \
    && npm install -g ionic-plugin-keyboard \
    && npm install -g cordova-plugin-whitelist \
    && npm install -g cordova-plugin-device \
    && npm install -g cordova-plugin-splashscreen \
    && npm install -g cordova-plugin-ionic-webview \
    && npm install -g karma-cli \
    && npm install -g yarn
