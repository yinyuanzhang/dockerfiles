FROM hashicorp/terraform:light

RUN apk --no-cache add jq zip openssl ansible

WORKDIR /app

COPY ./docker_entrypoint.sh /

ENTRYPOINT ["/docker_entrypoint.sh"]

