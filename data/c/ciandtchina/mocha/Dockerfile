FROM openjdk:latest

LABEL maintainer="jason@ciandt.com"

RUN apt-get install -y curl \
  && curl -sL https://deb.nodesource.com/setup_11.x | bash - \
  && apt-get install -y nodejs \
  && curl -L https://www.npmjs.com/install.sh | sh \
  && npm install  mocha -g

ENTRYPOINT [ "mocha" ]