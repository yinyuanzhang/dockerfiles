FROM alpine

ENV NAME=firthall
ADD ./build /build
ADD ./entrypoint /entrypoint

RUN apk --no-cache add bash

RUN bash < /entrypoint

