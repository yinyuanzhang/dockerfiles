FROM golang:1.12
RUN go get -u github.com/golang/dep/cmd/dep
RUN go get -u github.com/alecthomas/gometalinter
RUN gometalinter --install
RUN go get -u github.com/golangci/golangci-lint/cmd/golangci-lint
