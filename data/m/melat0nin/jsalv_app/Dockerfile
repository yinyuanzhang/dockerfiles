FROM node:10.1.0
MAINTAINER James Salvatore "jimmysalvatore.uc@gmail.com"

COPY . /app
WORKDIR /app

RUN npm i -S
RUN npm run build

CMD ["npm", "run", "start"]
