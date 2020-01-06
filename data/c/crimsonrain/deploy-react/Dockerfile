FROM node:current-alpine
RUN apk update && \
    apk add --no-cache git openssh-client python py-pip && \
    rm -rf /var/lib/apt/lists/* && \
    rm /var/cache/apk/* && \
    pip install awscli

ENTRYPOINT [ "sh" ]
