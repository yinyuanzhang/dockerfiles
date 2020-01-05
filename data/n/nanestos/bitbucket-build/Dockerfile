FROM maven:3.6.0-jdk-11

RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - && \
    apt-get install nodejs build-essential -y && \
    npm set strict-ssl false && \
    npm install -g npm@latest && \
    npm install -g bower grunt grunt-cli && \
    npm cache clear -f && \
    npm install -g n && \
    n stable

RUN npm install -g gulp

RUN apt-get update && apt-get install -y \
    python-pip \
    openssl \
    python2.7-dev
