FROM alpine

ENV NAME=homebrew-api
ADD ./build /build
ADD ./entrypoint /entrypoint

RUN apk --no-cache add bash

RUN bash < /entrypoint

