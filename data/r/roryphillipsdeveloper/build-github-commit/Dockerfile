FROM alpine:3.6
COPY publish-package.sh ~/publish-pachage.sh
WORKDIR ~/
RUN apk add --update \
    ca-certificates \
    git \
    bash
RUN rm -rf /var/cache/apk/*
RUN export PATH=$PATH:~/
