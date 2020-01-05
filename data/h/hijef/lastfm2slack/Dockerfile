FROM node:lts-alpine

WORKDIR /app
COPY src/logic src/logic
COPY src/model src/model
COPY src/rest src/helper
COPY app.js app.js
COPY package.json package.json
COPY yarn.lock yarn.lock

RUN yarn install --production=true

CMD ["yarn", "start"]