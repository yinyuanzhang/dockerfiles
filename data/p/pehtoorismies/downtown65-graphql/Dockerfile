FROM node:9.5.0-alpine

ENV WORKDIR=/home/node/app

WORKDIR ${WORKDIR}

COPY . ${WORKDIR}

RUN chown -R node:node ${WORKDIR}

USER node

RUN npm install

EXPOSE 4000

CMD [ "npm", "start" ]