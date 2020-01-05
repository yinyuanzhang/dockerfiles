FROM golang:alpine as build

# get our source
COPY . /go/src/app
WORKDIR /go/src/app

# must be completely static
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 \
    go build -a -installsuffix cgo \
    -ldflags="-s -w" \
    -o 404 \
    .


# include only our app
FROM scratch
COPY --from=build /go/src/app/404 /404
COPY LICENSE /LICENSE

# Don't run as root
USER 65534:65534

# run our app
ENTRYPOINT ["/404"]
CMD [":8080", "/health_check"]
