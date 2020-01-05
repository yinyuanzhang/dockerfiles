FROM alpine:latest

ENV CONSUL_VERSION=0.5.2

RUN apk --update add curl ca-certificates \
    && mkdir -p /tmp/src && cd /tmp/src \
    && curl -L -O https://circle-artifacts.com/gh/andyshinn/alpine-pkg-glibc/6/artifacts/0/home/ubuntu/alpine-pkg-glibc/packages/x86_64/glibc-2.21-r2.apk \
    && apk add --allow-untrusted glibc-2.21-r2.apk \
    && curl -L -O https://circle-artifacts.com/gh/andyshinn/alpine-pkg-glibc/6/artifacts/0/home/ubuntu/alpine-pkg-glibc/packages/x86_64/glibc-bin-2.21-r2.apk \
    && apk add --allow-untrusted glibc-bin-2.21-r2.apk \
    && /usr/glibc/usr/bin/ldconfig /lib /usr/glibc/usr/lib \
    && mkdir -p /usr/share/consul/bin /tmp/consul /etc/consul /etc/consul.d \
    && curl -L -O https://dl.bintray.com/mitchellh/consul/${CONSUL_VERSION}_linux_amd64.zip \
    && unzip ${CONSUL_VERSION}_linux_amd64.zip \
    && mv -f consul /usr/share/consul/bin/consul \
    && chmod +x /usr/share/consul/bin/consul \
    && ln -s /usr/share/consul/bin/consul /usr/bin/consul \
    && apk del --purge ca-certificates \
    && rm -rf /tmp/* /var/cache/apk/*


COPY client.json /etc/consul/client.json

EXPOSE 8301 8301/udp 8500 8600 8600/udp

WORKDIR /usr/share/consul/

ENTRYPOINT ["/usr/bin/consul", "agent", "-config-file=/etc/consul/client.json", "-config-dir=/etc/consul.d", "-data-dir=/tmp/consul"]
CMD []