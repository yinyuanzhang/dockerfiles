FROM debian:stable as build_env

RUN apt-get update
RUN apt-get install -y scrypt

FROM gcr.io/distroless/base-debian10

COPY --from=build_env /usr/bin/scrypt /usr/bin/scrypt

ENTRYPOINT ["/usr/bin/scrypt"]
