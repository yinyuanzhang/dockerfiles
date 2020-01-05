FROM golang as builder
RUN go get -u github.com/pressly/goose/cmd/goose
WORKDIR /go/src/github.com/pressly/goose/cmd/goose
RUN CGO_ENABLED=0 GOOS=linux go build -a -tags goose -o build/goose .

FROM alpine
COPY --from=builder /go/src/github.com/pressly/goose/cmd/goose/build/goose goose


