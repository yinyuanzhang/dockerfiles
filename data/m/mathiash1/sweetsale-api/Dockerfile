FROM node:11

RUN apt-get update
RUN apt-get install -y build-essential python
RUN apt-get install -y pdftk
RUN apt-get install -y nano

ENV NODE_ENV production

WORKDIR /app
COPY . /app
RUN npm i
RUN npm run build
CMD npm start

EXPOSE 4100 4101