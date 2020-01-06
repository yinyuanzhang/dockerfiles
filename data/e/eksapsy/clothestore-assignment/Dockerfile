FROM node:10.16-alpine

# App directory
RUN mkdir -p /opt/app
WORKDIR /opt/app

# Install yarn
RUN npm i yarn -g

# Copy app files
COPY ./web/public ./public
COPY ./web/package.json .
COPY ./web/yarn.lock .
COPY ./web/src ./src
COPY ./web/tsconfig.json .

# Install dependencies
RUN yarn

# Changed environment requires rebuild of node-sass
RUN npm rebuild node-sass

EXPOSE 3000

CMD [ "yarn", "start" ]