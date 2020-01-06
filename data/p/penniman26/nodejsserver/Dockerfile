FROM node:10.15.1

COPY ./package.json /app/
COPY ./package-lock.json /app/

RUN cd /app && npm install

COPY ./*.js /app/

CMD node /app/node-server.js
