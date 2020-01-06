FROM golang:1.9.7

ENV SHAMAN_COMMIT=7aa2eab

# git clone && go install instead of go get to force the commit above
RUN mkdir -p src/github.com/nanopack/shaman && \
    cd src/github.com/nanopack/shaman && \
    git clone https://github.com/nanopack/shaman.git . && \
    git checkout -b build "${SHAMAN_COMMIT}" && \
    go get -v . && \
    go install && \
    cd / && rm -rf /go/src

