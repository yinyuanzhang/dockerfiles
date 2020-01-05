FROM alpine

ENV NAME=prodection
ADD ./build /build
ADD ./entrypoint /entrypoint

RUN apk --no-cache add bash

RUN bash < /entrypoint

