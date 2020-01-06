FROM node:10-alpine

LABEL maintainer="gunjit93@gmail.com"

RUN apk update; \
	apk add --no-cache mongodb;

ENV MONGOMS_SYSTEM_BINARY=/usr/bin/mongod

WORKDIR /app

COPY package*.json ./

RUN npm cache clean --force; \
	npm install --no-package-lock

COPY . .

EXPOSE 8000

CMD ["node", "app/index.js"]
