FROM golang:1.11-alpine
RUN apk update && \
    apk add git nodejs-npm && \
    npm i -g npm && \
    go get -tags "v0.13.10" -u -v github.com/gobuffalo/buffalo/buffalo
