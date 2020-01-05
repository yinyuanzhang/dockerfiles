FROM golang:latest as builder
WORKDIR /go/src/github.com/ayunyan/omronups_exporter/
COPY *.go ./
RUN go get -d
RUN GOOS=linux go build -a -tags netgo -installsuffix netgo --ldflags '-extldflags "-static"' -o omronups_exporter .

FROM alpine:latest
COPY --from=builder /go/src/github.com/ayunyan/omronups_exporter/omronups_exporter /bin/omronups_exporter
EXPOSE 9430
CMD ["/bin/omronups_exporter"]
