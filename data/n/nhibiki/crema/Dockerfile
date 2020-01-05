FROM alpine:3.8
MAINTAINER NHibiki<i@yuuno.cc>

WORKDIR /crema-go
COPY . .

# Build Server Side
# sed -i 's/v3.8/edge/g' /etc/apk/repositories \
RUN apk add --no-cache ca-certificates musl-dev go git \
    && go get -d ./... \
    && go get github.com/json-iterator/go \
    && go build -tags=jsoniter -o crema . \
    && mv crema /usr/bin/crema \
    && rm /crema-go/* -rf \
    && apk del go git

EXPOSE 8038
ENTRYPOINT ["/usr/bin/crema"]