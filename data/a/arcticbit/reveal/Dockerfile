FROM node:10-alpine AS build
WORKDIR /reveal

RUN apk add git python make gcc
RUN git clone https://github.com/hakimel/reveal.js .
RUN npm install

FROM node:10-alpine
WORKDIR /reveal
COPY --from=build /reveal .

CMD npm start