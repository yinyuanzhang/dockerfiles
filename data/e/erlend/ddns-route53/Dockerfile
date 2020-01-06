FROM alpine

ENV VERSION=2.0.2
VOLUME /home/ddns/.aws

RUN apk add -U curl bind-tools bash python3 && \
    pip3 install --upgrade --no-cache-dir pip awscli && \
    curl -L https://github.com/mthssdrbrg/ddns-route53/archive/v$VERSION.tar.gz \
    | tar zx && \
    mv ddns-route53-$VERSION/ddns-route53 /usr/local/bin && \
    adduser -D ddns && \
    chown ddns:ddns /home/ddns/.aws && \
    apk del curl && \
    rm -rf ddns-route53-$VERSION /var/cache/apk/*

COPY entrypoint.sh /

USER ddns
ENTRYPOINT ["/entrypoint.sh"]
CMD ["-h"]
