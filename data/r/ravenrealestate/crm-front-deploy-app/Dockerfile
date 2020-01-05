FROM node:lts

# Create app directory
RUN mkdir -p /usr/src/app/deploy_app
WORKDIR /usr/src/app/deploy_app

# Install app dependencies
COPY package.json /usr/src/app/deploy_app/package.json

RUN npm i -g gulp
RUN yarn install

CMD [ "yarn", "run", "start" ]
