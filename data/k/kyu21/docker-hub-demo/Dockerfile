# node LTS version
FROM node:10.15.3

RUN useradd --user-group --create-home --shell /bin/false app &&\
  npm install -g npm

ENV HOME=/home/app

USER app
WORKDIR $HOME/demo
