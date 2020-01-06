FROM alpine:3.8

LABEL maintainer="nbadger@mintel.com"

RUN apk add --no-cache curl bash \
    && mkdir -p /opt \
    && curl -LJ -o /opt/wait-for-it.sh https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh \
    && chmod +x /opt/wait-for-it.sh

WORKDIR /opt

ENTRYPOINT ["/opt/wait-for-it.sh"]
