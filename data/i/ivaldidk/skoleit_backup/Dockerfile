FROM alpine

RUN apk add nodejs yarn paxctl --no-cache
RUN paxctl -cm `which node`

WORKDIR /app

COPY *.js *.json ./
COPY fetch ./fetch/

RUN yarn install

CMD [ "node", "index.js" ]