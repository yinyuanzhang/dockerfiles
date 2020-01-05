FROM alpine

ENV NAME=check_packer
ADD ./build /build
ADD ./entrypoint /entrypoint

RUN apk --no-cache add bash

RUN bash < /entrypoint

