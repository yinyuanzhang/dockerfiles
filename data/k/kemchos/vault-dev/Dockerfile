FROM debian:wheezy

ENV GOROOT /usr/local/go
ENV GOPATH /go
ENV PATH $PATH:$GOROOT/bin:$GOPATH/bin

RUN apt-get update && apt-get install -y wget make git \
  && mkdir -p /tmp/src \
  && cd /tmp/src \
  && wget --no-check-certificate https://storage.googleapis.com/golang/go1.4.linux-amd64.tar.gz \
  && tar zxvf /tmp/src/go1.4.linux-amd64.tar.gz -C /usr/local \
  && mkdir -p /go/src && mkdir -p /go/bin \
  && cd /go/src \
  && git clone https://github.com/hashicorp/vault.git \
  && cd vault \
  && make bootstrap \
  && make dev \
  && cp /go/bin/vault /usr/local/bin \
  && apt-get --purge autoremove -y wget make git \
  && apt-get clean && rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/* /tmp/src /usr/local/go /go

COPY config.hcl /opt/vault/

EXPOSE 8200

ENTRYPOINT [ "/usr/local/bin/vault" ]
CMD [ "server", "-config=/opt/vault/config.hcl" ]