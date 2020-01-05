FROM node

RUN mkdir -p /app
COPY package.json /app
WORKDIR ./app

RUN npm install
COPY . /app

RUN npm run production
RUN rm -rf ./Client

EXPOSE 3000
