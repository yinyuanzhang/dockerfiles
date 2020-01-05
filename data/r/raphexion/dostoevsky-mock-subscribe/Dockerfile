FROM node:9.11.1

RUN git clone https://github.com/Raphexion/dostoevsky-mock-subscribe.git /dostoevsky-ms
WORKDIR /dostoevsky-ms

RUN npm install

EXPOSE 3000

ENTRYPOINT ["node", "index.js"]
