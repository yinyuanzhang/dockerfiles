FROM golang:1.12.5

WORKDIR /go/src/github.com/PumpkinSeed/grafana-restore
COPY . .

RUN go get -v ./...
RUN go install -v ./...

ENTRYPOINT ["grafana-restore"]