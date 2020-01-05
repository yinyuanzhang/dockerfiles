FROM alpine

RUN apk add nodejs yarn paxctl --no-cache
RUN apk add arp-scan --no-cache --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing
RUN paxctl -cm `which node`

WORKDIR /app

ADD *.js ./
ADD *.json ./
ADD public ./public

RUN yarn install

CMD [ "node", "index.js" ]