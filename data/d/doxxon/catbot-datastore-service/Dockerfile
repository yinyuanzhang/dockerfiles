FROM node:latest
RUN npm install -g json-server
COPY . /usr/src/app
WORKDIR /usr/src/app
CMD ["json-server", "--watch", "db.json"]
