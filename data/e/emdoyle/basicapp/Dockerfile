FROM node:12

WORKDIR /app

COPY yarn.lock .
COPY package.json .

RUN npm install -g yarn serve

RUN yarn install --network-concurrency 1 --mutex network

COPY . .

RUN yarn build

EXPOSE 5000

CMD serve -s -l tcp://0.0.0.0:5000 build