FROM node:12

WORKDIR /home/lalauach/vera

COPY package.json yarn.lock ./

RUN yarn --frozen-lockfile

COPY . .

RUN yarn build

EXPOSE 80

ENV DOCKER="docker"

CMD [ "yarn", "start" ]