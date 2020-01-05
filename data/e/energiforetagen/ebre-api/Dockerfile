FROM node:12.4-alpine as builder

WORKDIR /app

COPY package* ./
RUN npm install -s

COPY . .

RUN node_modules/typescript/bin/tsc

FROM node:12.4-alpine as app

WORKDIR /app

COPY --from=builder /app/dist/src ./src

COPY package* ./
RUN npm install --production && rm -rf node_modules/aws-* node_modules/core-js /root/.npm

CMD npm run prod
