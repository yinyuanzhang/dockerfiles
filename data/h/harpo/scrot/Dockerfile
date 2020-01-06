FROM alpine:3.8

LABEL maintainer "Harpo Roeder <roederharpo@protonmail.ch>"

RUN apk add scrot 

WORKDIR /ctx

VOLUME ["/ctx"]

ENTRYPOINT ["scrot"]
