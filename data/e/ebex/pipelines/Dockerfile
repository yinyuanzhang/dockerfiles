FROM node:10-alpine

WORKDIR /root

ADD setup.sh .
RUN ./setup.sh && rm setup.sh

ENTRYPOINT ["/bin/bash", "-l"]
