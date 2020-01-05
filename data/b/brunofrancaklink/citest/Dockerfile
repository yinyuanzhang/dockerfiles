FROM node:12-alpine

# Create app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Install app dependencies
COPY package.json /usr/src/app/
COPY yarn.lock /usr/src/app/
RUN yarn install

# Env
ENV NODE_ENV production

# Bundle app source
COPY . /usr/src/app

# Clear the cache
RUN yarn cache clean

EXPOSE 3000
CMD [ "yarn", "dev" ]
