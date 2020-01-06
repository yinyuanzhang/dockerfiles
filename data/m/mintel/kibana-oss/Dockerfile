FROM docker.elastic.co/kibana/kibana-oss:7.4.1

LABEL maintainer="nbadger@mintel.com" \
      vendor="Mintel" \
      version="7.4.1" \
      vcs-url="https://github.com/mintel/kiban-oss"

# Install Any extra package here
ENV JQ_VERSION=1.5 \
    JQ_SHA256=c6b3a7d7d3e7b70c6f51b706a3b90bd01833846c54d32ca32f0027f00226ff6d

USER root

# jq
RUN set -e \
    && curl -L https://github.com/stedolan/jq/releases/download/jq-${JQ_VERSION}/jq-linux64 -o /tmp/jq \
    && cd /tmp \
    && echo "$JQ_SHA256  jq" | sha256sum -c \
    && mv jq /usr/local/bin \
    && chmod +x /usr/local/bin/jq


ADD wait-for-it.sh /opt/wait-for-it.sh
RUN chmod +x /opt/wait-for-it.sh

ADD docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh
WORKDIR /opt

USER kibana

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["/usr/local/bin/kibana-docker"]
