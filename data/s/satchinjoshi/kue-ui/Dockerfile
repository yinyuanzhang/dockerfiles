FROM node:10.13-alpine

WORKDIR /app
ADD . .

RUN yarn install

EXPOSE 3000

CMD ["node", "index.js"]
