FROM node:9.0
LABEL maintainer="Zorex Salvo <zorexsalvo@gmail.com>"

COPY package.json /opt/
WORKDIR /opt/

RUN npm install

RUN npm install -g http-server

COPY . /opt/
EXPOSE 8080

RUN npm run build

CMD ["http-server", "dist/"]
