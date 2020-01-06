FROM alpine:3.9

COPY git-clone.sh /
RUN apk --no-cache add --update git openssh && \
    addgroup -g 1000 -S git && \
    adduser -u 1000 -S git -G git

ENTRYPOINT ["/git-clone.sh"]

