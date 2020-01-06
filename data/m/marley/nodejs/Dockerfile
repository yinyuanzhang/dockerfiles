FROM node:latest

RUN apt-get update && apt-get install -qq -y vim git curl net-tools dnsutils gcc make

ENV PROJECT_PATH /project
RUN mkdir -p $PROJECT_PATH
RUN mkdir -p /usr/local/lib/node_modules/
RUN npm install -g npm@latest nodemon@latest

WORKDIR $PROJECT_PATH

USER root
CMD ["bash"]
