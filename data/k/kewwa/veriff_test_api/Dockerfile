FROM node:8
WORKDIR /veriff_test

RUN mkdir -p /veriff_test
COPY ./database /veriff_test/database
COPY ./api /veriff_test/api

COPY ./keys /veriff_test/keys

RUN cd api && yarn install
CMD cd api && NODE_ENV=production node ./index.js

EXPOSE 8080
