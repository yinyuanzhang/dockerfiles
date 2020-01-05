From node:alpine
WORKDIR /build

COPY ./package.json .
COPY ./package-lock.json .

RUN npm install -g quasar-cli@latest @vue/cli 
RUN npm install
