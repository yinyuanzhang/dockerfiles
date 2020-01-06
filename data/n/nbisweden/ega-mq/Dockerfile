FROM rabbitmq:3.7.8-management-alpine

ARG BUILD_DATE
ARG SOURCE_COMMIT

LABEL maintainer "EGA System Developers"
LABEL org.label-schema.schema-version="1.0"
LABEL org.label-schema.build-date=$BUILD_DATE
LABEL org.label-schema.vcs-url="https://github.com/EGA-archive/LocalEGA-mq"
LABEL org.label-schema.vcs-ref=$SOURCE_COMMIT

VOLUME /var/lib/rabbitmq

RUN apk add --no-cache ca-certificates

RUN rabbitmq-plugins enable --offline rabbitmq_federation rabbitmq_federation_management rabbitmq_shovel rabbitmq_shovel_management

COPY entrypoint.sh /usr/local/bin/ega-entrypoint.sh

RUN chmod +x /usr/local/bin/ega-entrypoint.sh

USER 100:101

ENTRYPOINT ["/usr/local/bin/ega-entrypoint.sh"]

CMD ["rabbitmq-server"]
