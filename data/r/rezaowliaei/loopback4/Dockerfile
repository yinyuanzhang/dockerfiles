FROM node
LABEL maintainer="r.owliaei@gmail.com"

RUN apt-get -y update && \
  apt-get -y dist-upgrade &&\
  apt-get clean &&\
  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/* &&\
  mkdir -p /usr/src/app &&\
  chown node:node /usr/src/app

ENV NPM_CONFIG_PREFIX=/home/node/.npm-global
ENV PATH=$PATH:/home/node/.npm-global/bin

WORKDIR /usr/src/app
USER node
RUN npm i -g @loopback/cli
ENTRYPOINT ["lb4"]
