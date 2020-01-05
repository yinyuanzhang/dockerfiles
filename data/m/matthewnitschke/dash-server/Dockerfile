FROM node:12.1.0

# RUN apk add --no-cache bash

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
ENV PATH /usr/src/app/node_modules/.bin:$PATH

RUN yarn global add parcel-bundler

COPY package.json /usr/src/app/package.json
RUN yarn install

COPY . /usr/src/app
RUN yarn build

CMD ["yarn", "start"]
