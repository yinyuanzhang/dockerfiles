FROM circleci/node:8.11.3

RUN sudo apt-get update && sudo apt-get install -y mysql-client

ENV NPM_CONFIG_PREFIX=/home/circleci/.npm-global
ENV PATH=/home/circleci/.npm-global/bin:$PATH

RUN npm i -g npm@6.1.0
RUN npm --version
# RUN /home/circleci/.npm-global/bin/npm --version