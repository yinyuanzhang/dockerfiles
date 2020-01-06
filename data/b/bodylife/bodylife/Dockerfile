FROM golang:1.12 AS builder

# Enable go modules
ENV GO111MODULE=on

# Set the working directory to the project path
WORKDIR /go/backend

# Copy project files
COPY . ./

# Set working direcory to project main
WORKDIR /go/backend/cmd/api

# Build and install project
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -a -installsuffix cgo -ldflags="-w -s" -o /go/bin/api -mod vendor

# Create executable image
FROM golang:1.12-alpine

# Copy the executable
COPY --from=builder /go/bin/api /opt/bodylife/

# Copy the google application credentials file
COPY --from=builder /go/backend/gcs-creds.json /opt/bodylife/

# Set path
ENV PATH=$PATH:/opt/bodylife

# Set google application credentials path
ENV GOOGLE_APPLICATION_CREDENTIALS=/opt/bodylife/gcs-creds.json

# Set public mailjet api key
ENV MJ_APIKEY_PUBLIC=0cf1358e7746b299927ac0d39552347b

# Set mailjet api secret
ENV MJ_APIKEY_PRIVATE=72643c718d5e08e32e1a4b75176248e4

# Expose api ports: http, ws, grpc
EXPOSE 5222 5322

# Set the entry point to the application executable
ENTRYPOINT ["api"]