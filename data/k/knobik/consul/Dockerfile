FROM alpine:3.4

ENV CONSUL_VERSION 1.3.0
ENV CONSUL_SHA256 a6896509b72fa229496b3adda51357c95d68a796ae3328d7d6a61195d6c68bac

RUN apk --no-cache add curl ca-certificates \
    && curl -sSL https://releases.hashicorp.com/consul/${CONSUL_VERSION}/consul_${CONSUL_VERSION}_linux_amd64.zip -o /tmp/consul.zip \
    && echo "${CONSUL_SHA256}  /tmp/consul.zip" > /tmp/consul.sha256 \
    && sha256sum -c /tmp/consul.sha256 \
    && cd /bin \
    && unzip /tmp/consul.zip \
    && chmod +x /bin/consul \
    && rm /tmp/consul.zip

ENTRYPOINT ["/bin/consul"]
