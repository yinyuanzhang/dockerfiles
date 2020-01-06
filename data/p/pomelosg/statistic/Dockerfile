# Start from golang v1.11 base image
FROM golang:1.12 as builder

# Add Maintainer Info
LABEL maintainer="Sun Zelun <sun.z@pg.com>"

# Build Args
ARG APP_NAME=statisticapi
ARG LOG_DIR=/${APP_NAME}/logs

# Create Log Directory
RUN mkdir -p ${LOG_DIR}

# Environment Variables
ENV LOG_FILE_LOCATION=${LOG_DIR}/app.log 

# Set the Current Working Directory inside the container
WORKDIR /go/src/github.com/sunzelun/statisticapi

# Copy everything from the current directory to the PWD(Present Working Directory) inside the container
COPY . .

# Download dependencies
RUN go get -d -v ./...
RUN go get -u github.com/golang/dep/cmd/dep
RUN dep ensure

# Build the Go app
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o /go/bin/statisticapi .


######## Start a new stage from scratch #######
FROM alpine:latest  

RUN apk --no-cache add ca-certificates

WORKDIR /root/

# Copy the Pre-built binary file from the previous stage
COPY --from=builder /go/bin/statisticapi .
COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/

EXPOSE 80
EXPOSE 443

# Declare volumes to mount
VOLUME ["/statisticapi/logs"]
VOLUME ["/cert-cache"]

CMD ["./statisticapi"]