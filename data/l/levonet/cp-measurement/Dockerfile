FROM node:lts-alpine

RUN mkdir -p /app
RUN mkdir -p /app/db
WORKDIR /app

ENV NODE_ENV="production"

COPY package*.json ./
RUN npm install --only=production

COPY configs /app/configs/
COPY lib /app/lib/
COPY index.js /app/index.js

EXPOSE 8080
ENTRYPOINT ["node", "index.js"]
