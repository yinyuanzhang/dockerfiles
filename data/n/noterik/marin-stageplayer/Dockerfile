FROM node:10.0-alpine as builder
WORKDIR /tmp

ARG command="yarn build:production"

RUN mkdir /app && chown node:node /app

#RUN apk add --update \
#    python \
#    make \
#    gcc \
#    g++ \
#  && rm -rf /var/cache/apk/*

COPY package.json yarn.lock /tmp/
RUN yarn install --ignore-optional --pure-lockfile

COPY . /app/
RUN cp -a /tmp/node_modules /app
ENV NODE_ENV=production
WORKDIR /app
RUN ${command}

FROM nginx:alpine
COPY --from=builder /app/dist/online /usr/share/nginx/html/
EXPOSE 80
