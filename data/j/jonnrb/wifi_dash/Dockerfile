from golang as build
workdir /go/src/github.com/jonnrb/wifi_dash
add . .
run go get -u github.com/golang/dep/cmd/dep \
 && dep ensure \
 && CGO_ENABLED=0 GOOS=linux go-wrapper install

from gcr.io/distroless/base
copy --from=build /go/bin/wifi_dash /wifi_dash
add index.html /
add static/bootstrap.min.css /static/bootstrap.min.css
entrypoint ["/wifi_dash"]
