FROM node:11.6

WORKDIR /home/aiuach/aiuach-server

COPY package.json yarn.lock ./

RUN yarn --frozen-lockfile

COPY .babelrc ./
COPY src ./src

RUN yarn build

COPY static ./static

EXPOSE 80 443

ENV DOCKER="docker"

CMD [ "yarn", "start" ]