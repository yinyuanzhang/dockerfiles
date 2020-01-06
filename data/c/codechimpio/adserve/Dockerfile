# This is a two-stage Docker build:
# https://docs.docker.com/develop/develop-images/multistage-build

#
# Build container
FROM golang:1.12.7 AS BUILDER

WORKDIR /go/src/github.com/bgv/adserve
COPY . .
RUN make all

# Runtime container
FROM alpine:latest
COPY --from=BUILDER /go/src/github.com/bgv/adserve/adserve /bin/adserve

EXPOSE     9090
VOLUME     [ "/adserve" ]
WORKDIR    /adserve
ENTRYPOINT [ "/bin/adserve" ]
CMD        [ "--images-path=/adserve", \
             "--db-path=/adserve/adserve.db" ]
