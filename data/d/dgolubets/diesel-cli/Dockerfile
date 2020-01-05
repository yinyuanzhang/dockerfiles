FROM alpine:edge
RUN apk add --update make bash python g++ postgresql-dev sqlite-dev mariadb-dev curl rust cargo
RUN cargo install diesel_cli --root /.cargo

FROM alpine:edge
WORKDIR /usr/app
RUN apk add --no-cache libgcc libpq sqlite-libs mariadb-connector-c
COPY --from=0 /.cargo/bin/diesel /usr/bin/
ENTRYPOINT ["diesel"]
