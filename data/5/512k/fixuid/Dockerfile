FROM alpine:latest
LABEL Description="fixuid binary file" Vendor="512k"

ENV FIXUID_VER 0.4

RUN set -xe \
    && wget "https://github.com/boxboat/fixuid/releases/download/v${FIXUID_VER}/fixuid-${FIXUID_VER}-linux-amd64.tar.gz" \
      -O /tmp/fixuid.tar.gz \
    && tar zxvf /tmp/fixuid.tar.gz -C /tmp \
    && mv "/tmp/fixuid" /usr/bin/fixuid \
    && chmod +x /usr/bin/fixuid \
    && rm -Rf "/tmp/fixuid" /tmp/rr.tar.gz \
    && ls -l /usr/bin/fixuid

ENTRYPOINT ["/usr/bin/fixuid"]
