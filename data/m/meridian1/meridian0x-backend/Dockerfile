# Stage 1
FROM node:11-alpine as yarn-install
WORKDIR /usr/src/app
# Install app dependencies
COPY package.json yarn.lock ./
RUN apk update && \
    apk upgrade && \
    apk add --no-cache --virtual build-dependencies bash git openssh python make g++ && \
    yarn --frozen-lockfile --no-cache && \
    apk del build-dependencies && \
    yarn cache clean

# Runtime container with minimal dependencies
FROM node:11-alpine
WORKDIR /usr/src/app
COPY --from=yarn-install /usr/src/app/node_modules /usr/src/app/node_modules
# Bundle app source
COPY . .

ENV HTTP_PORT=3000
ENV NETWORK_ID=1
ENV FEE_RECIPIENT=0x7178DE2cEaE29Ba628Bb2e22C9c877b9c5eE3797
ENV MAKER_FEE_ZRX_UNIT_AMOUNT=.1
ENV TAKER_FEE_ZRX_UNIT_AMOUNT=.3
ENV RPC_URL=https://mainnet.infura.io/v3/3ae21d5233594d48b4475cfb9afb3ab7
ENV WHITELIST_ALL_TOKENS=true

RUN yarn build

EXPOSE 3000
CMD [ "./node_modules/.bin/forever", "ts/lib/index.js" ]
