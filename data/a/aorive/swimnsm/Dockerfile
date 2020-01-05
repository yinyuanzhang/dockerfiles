# Golang version
ARG goversion=1.12.3

## BUILD STAGE
FROM golang:${goversion}-stretch AS build-env
# Go build flags
ENV CGO_ENABLED=0 GO111MODULE=on
ENV GOOS=linux GOARCH=arm GOARM=7
# Copy swimnsm library
WORKDIR /src/swimnsm/
COPY internal/ internal/
COPY pkg/ pkg/
COPY go.mod go.sum ./
# Copy the command
WORKDIR cmd/k8s/
COPY cmd/k8s/ ./
# Compile the command
RUN go build -i -o /bin/app .

## FINAL STAGE
FROM scratch
# Copy the executable
COPY --from=build-env /bin/app /
# Expose port
EXPOSE 32896/udp
# Define the entrypoint
ENTRYPOINT ["/app"]