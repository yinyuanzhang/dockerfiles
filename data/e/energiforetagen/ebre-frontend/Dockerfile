FROM node:12.4-alpine

WORKDIR /app

COPY package* ./
RUN npm ci -s --production
RUN npm install -g --s serve

COPY public public
COPY src src
COPY tsconfig.json ./
COPY serve.json ./

CMD npm run build && serve -s
