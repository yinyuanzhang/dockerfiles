# Cowsay Container - v7
# docker run -it -v /tmp:/cow cindychao14/cowsay:v4 bash

FROM alpine:3.6

MAINTAINER cindychao14

RUN apk add --no-cache perl 

COPY cowsay /usr/bin/cowsay 
COPY default.cow /usr/share/cowsay/default.cow 

CMD ["/usr/bin/cowsay","Testing"]
