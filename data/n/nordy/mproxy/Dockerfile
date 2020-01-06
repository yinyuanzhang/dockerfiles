FROM alpine:3.8 as build

RUN apk add --no-cache alpine-sdk

COPY mproxy.c /mproxy/
COPY Makefile /mproxy/
WORKDIR /mproxy
RUN make

FROM alpine:3.8
COPY --from=build /mproxy/mproxy /bin/mproxy
ENTRYPOINT ["/bin/mproxy"]
