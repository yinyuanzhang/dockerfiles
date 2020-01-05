FROM alpine

ENV NAME=sequest-jata
ADD ./build /build
ADD ./entrypoint /entrypoint

RUN apk --no-cache add bash

RUN bash < /entrypoint

