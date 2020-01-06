FROM alpine

ENV NAME=drupal_ver_repo
ADD ./build /build
ADD ./entrypoint /entrypoint

RUN apk --no-cache add bash

RUN bash < /entrypoint

