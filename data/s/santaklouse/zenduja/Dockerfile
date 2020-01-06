FROM node:10

ENV NODE_VERSION 10.6.0
ENV NPM_VERSION 6.1.0

# Create app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Install app dependencies
#COPY package.json /usr/src/app/

# Bundle app source
COPY . /usr/src/app

RUN npm install
RUN npm rebuild node-sass
RUN npm run build

EXPOSE 80 9229
CMD [ "npm", "start" ]
