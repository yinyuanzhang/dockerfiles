FROM nginx:1.13.5
MAINTAINER Archie Lee <achi@987.tw>

ENV CONSUL_TEMPLATE_VERSION 0.19.3

RUN DEBIAN_FRONTEND=noninteractive \
    apt-get update -qq && \
    apt-get -y install wget runit unzip && \
    rm -rf /var/lib/apt/lists/*

RUN wget https://releases.hashicorp.com/consul-template/${CONSUL_TEMPLATE_VERSION}/consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip
RUN unzip -d /usr/local/bin consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip

COPY nginx.service /etc/service/nginx/run
COPY consul-template.service /etc/service/consul-template/run

RUN mkdir /etc/consul-template && chmod +x /etc/service/nginx/run && chmod +x /etc/service/consul-template/run

CMD ["/usr/bin/runsvdir", "/etc/service"]

