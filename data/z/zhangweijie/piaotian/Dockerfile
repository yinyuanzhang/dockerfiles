FROM node:8-alpine
ENV NODE_ENV production
WORKDIR /usr/src/app
COPY ["package.json", "yarn.lock", "./"]
RUN yarn --production --silent
COPY . .
RUN yarn build
EXPOSE 3000
CMD yarn start