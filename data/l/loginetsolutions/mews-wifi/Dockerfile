FROM golang:alpine as builder

# Add Maintainer Info
LABEL maintainer="Maxim Donchenko <maximd@loginet.ee>"

# Set the Current Working Directory inside the container
WORKDIR /go/src/github.com/mobmax/mews-wifi

# Copy everything from the current directory to the PWD(Present Working Directory) inside the container
COPY . .

RUN apk add --update gcc musl-dev
RUN apk add --no-cache git

# Download dependencies
RUN go get -d -v ./...

# Build the Go app
RUN GOOS=linux go build -a -installsuffix cgo -o /go/bin/mews-wifi .

######## Start a new stage from scratch #######
FROM alpine:latest

RUN apk --no-cache add ca-certificates


WORKDIR /root/

# Copy the Pre-built binary file from the previous stage
COPY --from=builder /go/bin/mews-wifi .

# Build Args
ARG APP_NAME=mews-wifi
ARG LOG_DIR=/${APP_NAME}/logs
ARG DB_DIR=/freeradius-server/db

# Environment Variables
ENV LOG_FILE_LOCATION=${LOG_DIR}/mews-wifi.log
ENV RADIUS_DB_PATH=${DB_DIR}/freeradius.db

ENV CLIENT_TOKEN=E0D439EE522F44368DC78E1BFB03710C-D24FB11DBE31D4621C4817E028D9E1D
# ENV ACCESS_TOKEN=C66EF7B239D24632943D115EDE9CB810-EA00F8FD8294692C940F6B5A8F9453D
# ENV SENDER_NAME=meetingserver@loginet.ee
# ENV SENDER_PASSWORD=MyHyHaygyij6
# ENV SMTP_SERVER=mail.loginet.ee

# Create Log Directory
RUN mkdir -p ${LOG_DIR}
RUN mkdir -p ${DB_DIR}

# Declare volumes to mount
VOLUME ["/freeradius-server/db"]
VOLUME ["/mews-wifi/logs"]

# Run the binary program produced by `go install`
CMD ["./mews-wifi"]
