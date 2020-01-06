FROM golang:1.10 AS deps

COPY dependencies.txt /
RUN mkdir -p /go/src; cat /dependencies.txt | xargs go get -v

FROM golang:1.10 AS build
COPY --from=deps /go/src /go/src
COPY replicator /go/src/replicator
WORKDIR /go/src/replicator
RUN chmod +x build.sh && go get -v ./...
WORKDIR /go/src/replicator
RUN ./build.sh

FROM scratch
LABEL maintainer="Bojan Cekrlic"

COPY --from=build /go/src/replicator/target/replicator-linux-amd64 /usr/local/bin/replicator

CMD ["/usr/local/bin/replicator"]
