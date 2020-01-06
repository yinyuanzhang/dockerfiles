# Build client
FROM node:latest as client-builder

RUN apt-get update && \
    apt-get install apt-transport-https -y

RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
    echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list && \
    apt-get update && \
    apt-get install --no-install-recommends yarn -y

RUN yarn global add webpack webpack-cli

WORKDIR /app
COPY . /app

RUN yarn install --production=false
RUN npm run build

# Deploy runtime
FROM nginx:stable-alpine

WORKDIR /usr/share/nginx/html
COPY --from=client-builder /app/dist .
