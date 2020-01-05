FROM golang:1.12
RUN curl https://glide.sh/get | sh
RUN go get -u github.com/alecthomas/gometalinter
RUN gometalinter --install
RUN go get -u github.com/golangci/golangci-lint/cmd/golangci-lint
