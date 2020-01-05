FROM arm32v7/openjdk:8-jre-alpine

COPY qemu-arm-static /usr/bin

RUN apk update && apk upgrade
RUN apk add unrar p7zip bash

CMD ["/bin/bash"]
