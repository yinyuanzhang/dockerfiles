FROM node:8.11.3-alpine

WORKDIR /opt/buhane/mock-server

COPY . /opt/buhane/mock-server

RUN npm install -g json-server

EXPOSE 6060

ENTRYPOINT ["json-server", "--watch", "db.json"]
