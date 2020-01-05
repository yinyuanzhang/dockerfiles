FROM node:8
WORKDIR /veriff_test

RUN mkdir -p /veriff_test
COPY ./database /veriff_test/database
COPY ./web /veriff_test/web

COPY ./keys /veriff_test/keys
COPY ./translations /veriff_test/translations

RUN cd web && yarn install
RUN cd web && yarn run build
CMD cd web && NODE_ENV=production node ./server/bootstrap.js

EXPOSE 3000