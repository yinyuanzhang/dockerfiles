FROM rancher/cli:latest

RUN apk add --no-cache curl

COPY entrypoint.sh /

ENTRYPOINT ["/entrypoint.sh"]
