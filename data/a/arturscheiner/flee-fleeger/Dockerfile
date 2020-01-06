# Smallest base image
FROM alpine:latest

LABEL maintainer="Artur Scheiner <artur.scheiner@gmail.com>"

RUN mkdir -p /flee/bin && \
    apk add nodejs && \
    cd /flee/bin

ADD fleeger /flee/bin
ADD FLEE_VERSION /flee/bin
ADD oui.txt /flee/bin
ADD fleedec /flee/bin/fleedec

WORKDIR /flee/bin
CMD ["/flee/bin/fleeger","--address","0.0.0.0:33514"]
