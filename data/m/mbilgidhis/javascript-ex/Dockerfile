FROM node:10-alpine

WORKDIR .

COPY package*.json ./

COPY index.js ./

RUN npm install

EXPOSE 3000

CMD ["node", "index.js"]