FROM node as builder

COPY . /usr/local/share/discord/
WORKDIR /usr/local/share/discord/

RUN yarn
RUN yarn build:prod

###
FROM node:alpine

COPY --from=builder /usr/local/share/discord/dist /usr/local/share/discord/dist
COPY package.json yarn.lock /usr/local/share/discord/
RUN chown node:node -R /usr/local/share/discord/

WORKDIR /usr/local/share/discord/

USER node:node

RUN yarn --production
ENTRYPOINT yarn start