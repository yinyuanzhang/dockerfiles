FROM node:10.16.0-jessie

WORKDIR /opt

ENV PORT=8000 \
    HOST=authen-service \
    NODE_ENV=production \
    MONGO_URL=mongo://mongodb:27017/authen-service \
    RABBIT_URL=amqp://rabbit:rabbit@rabbitmq:5672/comspaces \
    PRIVATE_KEY_PATH=/etc/deployment/privateKey.pem \
    PUBLIC_KEY_PATH=/etc/deployment/publicKey.pem \
    JWT_PRIVATE_KEY_PATH=/etc/deployment/privateKey.pem \
    JWT_PUBLIC_KEY_PATH=/etc/development/publicKey.pem

COPY package*.json /opt/

RUN apt-get update && apt-get install -y build-essential python \
  && npm install node-gyp node-pre-gyp \
  && npm rebuild bcrypt --build-from-source

RUN npm install --production
RUN npm install bcrypt@3.0.6

COPY . .

EXPOSE 8000

CMD ["node", "src/bootstrap.js"]
