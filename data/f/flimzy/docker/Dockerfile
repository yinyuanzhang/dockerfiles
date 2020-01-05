FROM flimzy/gopherjs:1.12

# Install gometalinter
RUN go get -u gopkg.in/alecthomas/gometalinter.v2 && gometalinter.v2 --install

# Install golangci-lint
RUN curl -sfL https://install.goreleaser.com/github.com/golangci/golangci-lint.sh | sh -s -- -b $(go env GOPATH)/bin v1.16.0
