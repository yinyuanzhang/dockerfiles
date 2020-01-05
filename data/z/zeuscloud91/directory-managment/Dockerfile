FROM node:10

WORKDIR /

COPY package.json ./

RUN npm install

COPY . .

EXPOSE 8084

CMD [ "node", "index.js" , "8084"]
