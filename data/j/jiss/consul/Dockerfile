FROM            jiss/dist
MAINTAINER      Anton Iskov <aiskov@jiss-software.com>

ENV CONSUL_VERSION 0.6.4

# Install
ADD https://releases.hashicorp.com/consul/${CONSUL_VERSION}/consul_${CONSUL_VERSION}_linux_amd64.zip /tmp/consul.zip
WORKDIR /bin
RUN unzip /tmp/consul.zip
RUN chmod +x /bin/consul
RUN rm /tmp/consul.zip

# Run
EXPOSE 8300 8301 8301/udp 8302 8302/udp 8400 8500 53/udp

VOLUME ["/data"]

ENV SHELL /bin/bash

ENTRYPOINT ["/bin/consul", "agent", "-server", "-data-dir=/tmp"]
CMD []
