FROM golang:1.10.3

RUN mkdir -p /go/bin && \
    go get -d -u github.com/golang/dep && \
    cd $(go env GOPATH)/src/github.com/golang/dep && \
    DEP_LATEST=$(git describe --abbrev=0 --tags) && \
    git checkout $DEP_LATEST && \
    go install -ldflags="-X main.version=$DEP_LATEST" ./cmd/dep
