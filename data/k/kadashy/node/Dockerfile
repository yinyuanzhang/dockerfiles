FROM node:10.14.2

RUN apt-get update && apt-get install -y \
    gpg

RUN npm install -g @angular/cli

RUN npm install pg@6.1.0

WORKDIR /usr/src/app

ARG NODE_ENV
ENV NODE_ENV $NODE_ENV
RUN npm install
COPY . /usr/src/app

CMD [ "npm", "start" ]

EXPOSE 443
EXPOSE 80
