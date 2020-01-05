FROM node:latest

MAINTAINER John Lin <linton.tw@gmail.com>

ENV HOME /root

# Define working directory for adding source.
WORKDIR /root

ADD . app-info-server

WORKDIR /root/app-info-server

RUN npm install

CMD ["npm", "start"]
