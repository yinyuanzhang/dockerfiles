FROM golang as BUILD

WORKDIR /go/src/app

COPY beansync.go .

RUN go get -v -d .

RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o beansync .

FROM shurshun/alpine-moscow

COPY --from=BUILD /go/src/app/beansync /

RUN chmod +x /beansync

ENTRYPOINT ["/beansync"]