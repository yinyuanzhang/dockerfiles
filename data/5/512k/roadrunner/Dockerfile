FROM alpine:latest
LABEL Description="high-performance PHP application server, load balancer and process manager" Vendor="512k"

RUN set -xe \
    && export RR_VERSION=${RR_VERSION:-`wget -qO - "https://api.github.com/repos/spiral/roadrunner/releases/latest" \
      | grep '"tag_name":' \
      | sed -E 's/.*"v([^"]+)".*/\1/'`} \
    && wget "https://github.com/spiral/roadrunner/releases/download/v${RR_VERSION}/roadrunner-${RR_VERSION}-linux-amd64.tar.gz" \
      -O /tmp/rr.tar.gz \
    && tar zxvf /tmp/rr.tar.gz -C /tmp \
    && mv "/tmp/roadrunner-${RR_VERSION}-linux-amd64/rr" /usr/bin/rr \
    && rm -Rf "/tmp/roadrunner-${RR_VERSION}-linux-amd64" /tmp/rr.tar.gz \
    && rr -v

EXPOSE 80
EXPOSE 443

ENTRYPOINT ["/usr/bin/rr"]
