FROM node:9.11.1-alpine

ENV KONG_GATEWAY="localhost:8001"

WORKDIR /home

COPY package.json ./

RUN npm install --quiet --production

COPY --chown=node:node src ./src


CMD ["npm", "run", "start"]