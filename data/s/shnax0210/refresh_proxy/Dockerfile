FROM node

WORKDIR /app

COPY . /app

RUN npm install http-proxy --save
RUN npm install minimist --save

EXPOSE 8081

ENTRYPOINT ["node", "proxy.js"]