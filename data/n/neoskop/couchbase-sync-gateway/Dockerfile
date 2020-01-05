FROM couchbase/sync-gateway:1.4.0-2
LABEL maintainer "devops@neoskop.de"
ENV DOCKERIZE_VERSION=v0.4.0 \
    COUCHBASE_HOSTNAME=couchbase \
    BUCKET=default
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz
COPY sync-gateway-config.tmpl /etc/sync_gateway/config.tmpl
COPY entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
