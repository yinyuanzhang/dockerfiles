FROM postgres:11-alpine

RUN apk add --no-cache bash

COPY docker-healthcheck /usr/local/bin/

HEALTHCHECK --interval=1s --retries=30 CMD ["docker-healthcheck"]
