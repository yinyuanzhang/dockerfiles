FROM alpine:3.8

ARG GIT_VERSION=2.18.1
ENV GIT_VERSION=${GIT_VERSION}

RUN apk --no-cache upgrade                        && \
    apk --no-cache add                               \
    sshpass openssh-client bash openssh              \
    git=${GIT_VERSION}-r0                         && \
    rm -rf /tmp/*                                 && \
    adduser -D git

USER git
