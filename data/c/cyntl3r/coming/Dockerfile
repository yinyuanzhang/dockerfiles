FROM node:alpine

ENV PORT="80"
ENV LOCALE="en"
ENV PAGE_TITLE="Coming Soon"
ENV HEADING_TEXT="Coming Soon"
ENV COUNTDOWN_DATE="2020-01-01"

WORKDIR /coming

COPY ./package*.json ./
RUN apk add --no-cache make gcc g++ python && \
  npm install && \
  apk del make gcc g++ python

COPY ./ ./
RUN npm run build

EXPOSE ${PORT}
CMD npm run start
