FROM node:8.11

LABEL maintainer = "Eden Cadagiani <e.cadagiani@gmail.com>"

ENV PORT 3000

WORKDIR /home/node/app
ADD package.json package.json
RUN npm install

COPY . /home/node/app

EXPOSE $PORT

CMD npm start
