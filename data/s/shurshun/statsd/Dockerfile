FROM node:alpine

LABEL SERVICE_NAME="statsd"

LABEL maintainer "4lifenet@gmail.com"
LABEL author "Korviakov Andrey"

HEALTHCHECK --interval=1m --timeout=2s \
  CMD [[ $(echo "health" | nc localhost 8126 | awk '{print $2}') == "up" ]] || exit 1

RUN \
    apk add --no-cache --update \
        ca-certificates \
        tzdata \
        curl \
        jq \
    && ln -fs /usr/share/zoneinfo/Europe/Moscow /etc/localtime \
    && CONSUL_TEMPLATE_VERSION=$(curl -s https://api.github.com/repos/hashicorp/consul-template/tags | jq -r ".[0] .name" | tr -d v) \
    && curl -fSl https://releases.hashicorp.com/consul-template/${CONSUL_TEMPLATE_VERSION}/consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.tgz | tar -C /bin -zx

RUN \
    apk add --no-cache --update --virtual .build-deps \
        git \
    && git clone https://github.com/etsy/statsd.git /app \
    && apk del .build-deps

WORKDIR /app

RUN npm install

COPY conf/ /app

EXPOSE 8125/udp
EXPOSE 8126

ENTRYPOINT [ "consul-template", "-config", "consul.hcl"]
