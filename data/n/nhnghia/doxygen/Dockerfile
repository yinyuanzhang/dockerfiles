FROM alpine:latest

MAINTAINER nhnghia@me.com

RUN set -eux; \
apk --no-cache add doxygen graphviz ttf-freefont

ENTRYPOINT ["doxygen"]

CMD [ "doxygen" ]

WORKDIR /data
VOLUME ["/data"]

