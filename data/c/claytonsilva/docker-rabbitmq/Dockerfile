FROM rabbitmq:3.7-management-alpine

ENV CREDSTASH_VERSION=v0.3.3

RUN apk update && apk add wget ca-certificates
#install gcredstash
RUN mkdir -p /opt/bin && \
    wget -O - https://github.com/winebarrel/gcredstash/releases/download/$CREDSTASH_VERSION/gcredstash-$CREDSTASH_VERSION-linux-amd64.gz | gunzip -c  > /opt/bin/gcredstash && \
    chmod 775 /opt/bin/gcredstash

COPY docker-entrypoint.sh /usr/local/bin/
COPY definitions.json /var/lib/rabbitmq/
RUN ln -s usr/local/bin/docker-entrypoint.sh / # backwards compat
RUN chmod 775 usr/local/bin/docker-entrypoint.sh

ENTRYPOINT ["usr/local/bin/docker-entrypoint.sh"]

EXPOSE 4369 5671 5672 25672
CMD ["rabbitmq-server"]
