# go バイナリをalpineインストール済み状態から持ってくる
FROM golang:1.12.4-alpine as gobinary

# docker:18.06.3
FROM docker:18.06.3-ce-dind

# ビルド用ツールとaws-cliの追加
RUN apk update && apk upgrade && \
    apk add --no-cache bash jq git make ca-certificates py-pip python && \
    /bin/bash -c "shopt -s dotglob" && \
    pip install --upgrade pip && \
    pip install awscli && \
    apk del --purge py-pip

# golang image からgoを持ってくる
COPY --from=gobinary /usr/local/go /usr/local/go

# Go用の環境変数のセット
ENV GOPATH=/go 
ENV PATH=$GOPATH/bin:/usr/local/go/bin:$PATH

# Go用のツールインストール
RUN mkdir -p "$GOPATH/src" "$GOPATH/bin" && \
    go get -u github.com/golang/dep/cmd/dep && \
    go get -u golang.org/x/lint/golint

WORKDIR /go

CMD ["/bin/bash"]
