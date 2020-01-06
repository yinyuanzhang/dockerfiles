FROM golang:latest as builder
ENV CGO_ENABLED=0
ENV GO111MODULE=on
RUN git clone https://github.com/kubernetes/sample-apiserver /wardle
WORKDIR /wardle
RUN go mod download
RUN go build -o /wardle/wardle .

FROM alpine
COPY --from=builder /wardle/wardle /wardle
ENTRYPOINT ["/wardle"]
