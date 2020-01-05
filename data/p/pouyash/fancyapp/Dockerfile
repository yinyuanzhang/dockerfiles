# Base build image
FROM golang:latest AS builder
ADD . /app/ 
WORKDIR /app 

RUN go mod download
 
#In this last stage, we start from a fresh Alpine image, to reduce the image size and not ship the Go compiler in our production artifacts.
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo  \
  -ldflags "-X main.buildstamp=`date -u '+%Y-%m-%d_%H:%M:%S'` -X main.buildhash=`git rev-parse HEAD`" \
  -o /go/bin/app .



FROM scratch
WORKDIR /
COPY --from=builder /go/bin/app .
CMD ["/app"]