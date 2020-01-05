FROM node:boron-alpine

EXPOSE 80

WORKDIR /app

COPY . .

RUN npm install

ENTRYPOINT ["/app/entry.sh"]