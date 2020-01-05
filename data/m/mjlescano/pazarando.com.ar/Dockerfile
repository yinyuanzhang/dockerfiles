FROM node:8-alpine

LABEL name="pazarando.com.ar"

MAINTAINER Matías Lescano <mjlescano@protonmail.com>

COPY ["package.json", "package-lock.json", "/usr/src/"]

WORKDIR /usr/src

ENV NODE_ENV=production

RUN npm install --loglevel warn

COPY [".", "/usr/src/"]

RUN npm run build

EXPOSE 3000

CMD ["npm", "start"]
