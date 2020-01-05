FROM amd64/alpine:3.8

WORKDIR /app

RUN addgroup -S databox && adduser -S -g databox databox && \
apk --no-cache add build-base pkgconfig nodejs npm libzmq zeromq-dev libsodium-dev python  && \
npm install zeromq@4.6.0 --zmq-external --verbose && \
apk del build-base pkgconfig libsodium-dev python zeromq-dev


COPY /package.json /app/package.json
RUN npm install
COPY / /app/
RUN npm run build
USER databox

LABEL databox.type="app"


EXPOSE 8080

CMD ["node","./server.js"]