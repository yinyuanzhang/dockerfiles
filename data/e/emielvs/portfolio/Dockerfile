FROM node:10

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . .

WORKDIR /usr/src/app/frontend
RUN yarn install --frozen-lockfile && yarn build

WORKDIR /usr/src/app/backend
RUN yarn install --frozen-lockfile
CMD ["node", "./src/server.js"]
