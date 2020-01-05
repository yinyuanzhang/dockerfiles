FROM alpine:3.11.2 AS builder

# Update/Upgrade/Add packages for building

RUN apk add --no-cache bash git go build-base

# Install go-init

WORKDIR /build/go-init

ENV GOPATH=/build/go-init/gospace

RUN go get -u github.com/betterplace/go-init

FROM node:13-alpine3.11 AS runner

# Update/Upgrade/Add packages

RUN apk add --no-cache bash ca-certificates

ARG APP_DIR=/app

RUN adduser -h ${APP_DIR} -s /bin/bash -D appuser

COPY --from=builder --chown=appuser:appuser /build/go-init/gospace/bin/go-init /opt/bin/

ENV PATH /opt/bin:${PATH}

WORKDIR ${APP_DIR}

COPY --chown=appuser:appuser . ${APP_DIR}

EXPOSE 3000

RUN /usr/local/bin/yarn --network-timeout 1000000 --network-concurrency 4

RUN patch -p0 < ws.patch

CMD [ "/opt/bin/go-init", "-main", "./start.sh" ]
