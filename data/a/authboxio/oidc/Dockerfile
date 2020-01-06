FROM node:12 as builder

ARG NODE_ENV
ENV NODE_ENV $NODE_ENV

RUN mkdir /app
WORKDIR /app

COPY package*.json ./

RUN npm install

FROM node:12-slim

RUN npm install -g pm2

WORKDIR /app

COPY --from=builder /app/node_modules node_modules

COPY . .

CMD ["pm2-runtime", "start", "src/index.js", "--env", "production"]
