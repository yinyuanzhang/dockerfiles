FROM alpine:3.10 AS dockerize

RUN apk add --no-cache openssl

ENV DOCKERIZE_VERSION v0.6.1
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz


FROM ubercadence/server:0.5.9 AS cadence


FROM alpine:3.10

RUN apk add --update --no-cache ca-certificates tzdata bash curl

ENV CADENCE_HOME /etc/cadence
RUN mkdir -p /etc/cadence

# libc is required because Cadence is built with cgo
RUN apk add --update --no-cache libc6-compat

COPY --from=dockerize /usr/local/bin/dockerize /usr/local/bin
COPY --from=cadence /cadence/cadence-cassandra-tool /usr/local/bin
COPY --from=cadence /cadence/cadence-sql-tool /usr/local/bin
COPY --from=cadence /cadence/cadence /usr/local/bin
COPY --from=cadence /cadence/cadence-server /usr/local/bin
COPY --from=cadence /cadence/schema /etc/cadence/schema

WORKDIR /etc/cadence

# Backward compatibility
RUN mkdir -p /cadence
COPY --from=cadence /cadence/cadence-cassandra-tool /cadence
COPY --from=cadence /cadence/cadence-sql-tool /cadence
COPY --from=cadence /cadence/cadence /cadence
COPY --from=cadence /cadence/cadence-server /cadence
COPY --from=cadence /cadence/schema /cadence/schema
