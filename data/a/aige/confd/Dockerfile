FROM alpine:3.2

ENV CONFD_VERSION 0.11.0
ADD https://github.com/kelseyhightower/confd/releases/download/v${CONFD_VERSION}/confd-${CONFD_VERSION}-linux-amd64 /
RUN mv /confd-${CONFD_VERSION}-linux-amd64 /usr/local/bin/confd && \
    chmod +x /usr/local/bin/confd

ENTRYPOINT ["/usr/local/bin/confd"]
