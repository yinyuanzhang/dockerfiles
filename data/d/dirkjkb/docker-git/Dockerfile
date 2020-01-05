FROM docker:18.09

RUN apk add --no-cache bash sed grep coreutils
RUN apk --update add git openssh && \
rm -rf /var/lib/apt/lists/* && \
rm /var/cache/apk/*
