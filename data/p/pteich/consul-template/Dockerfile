FROM alpine:3.5

MAINTAINER Peter Teich <mail@pteich.xyz>

ENV GOSU_VERSION 1.10
ENV DUMB_INIT_VERSION 1.2.0
ENV CONSUL_TEMPLATE_VERSION 0.19.0

RUN addgroup -S consul && adduser -S -G consul consul

RUN set -x \
    && apk update && apk add --no-cache --virtual .deps \
        openssl curl dpkg ca-certificates \
    && update-ca-certificates \        
    && cd /tmp \
    && dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')" \
    && curl -Ls https://github.com/tianon/gosu/releases/download/${GOSU_VERSION}/gosu-${dpkgArch} > /usr/bin/gosu \
    && curl -Ls https://github.com/Yelp/dumb-init/releases/download/v${DUMB_INIT_VERSION}/dumb-init_${DUMB_INIT_VERSION}_${dpkgArch} > /usr/bin/dumb-init \
    && chmod +x /usr/bin/gosu \
    && chmod +x /usr/bin/dumb-init \    
    && curl -Ls https://releases.hashicorp.com/consul-template/${CONSUL_TEMPLATE_VERSION}/consul-template_${CONSUL_TEMPLATE_VERSION}_linux_${dpkgArch}.zip > /tmp/consul-template.zip \
    && unzip consul-template.zip \
    && mv consul-template /usr/bin/consul-template \
    && chmod +x /usr/bin/consul-template \
    && apk del .deps

RUN mkdir /data && chown consul:consul /data
VOLUME ["/data"]

WORKDIR /data

ENTRYPOINT ["gosu", "consul", "dumb-init", "consul-template"]

CMD [""]
