FROM node:9.11-alpine

WORKDIR /app
COPY . /app

RUN npm install --only=production

EXPOSE 8080
CMD ["node", "server.js"]
