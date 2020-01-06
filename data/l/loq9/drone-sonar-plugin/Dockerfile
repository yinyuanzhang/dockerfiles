#FROM golang:1.13.0-alpine3.10 as build
FROM debian:buster-slim as build

# Set the Current Working Directory inside the container
WORKDIR /app

# Install dependencies
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y \
    bash \
    git \
    golang
#RUN apk update && apk upgrade && apk add --no-cache \
#  bash \ 
#  git

# Copy go mod and sum files
COPY go.mod go.sum ./

# Download all dependencies. Dependencies will be cached if the go.mod and go.sum files are not changed
RUN go mod download

# Copy the source from the current directory to the Working Directory inside the container
COPY . .

# Build the Go app
ENV GOOS linux
ENV GARCH amd64
ENV CGO_ENABLED 0

RUN go build -ldflags="-s -w" -o drone-sonar .

FROM openjdk:11-slim

ARG SONAR_VERSION=4.2.0.1873
ARG SONAR_SCANNER_CLI=sonar-scanner-cli-${SONAR_VERSION}
ARG SONAR_SCANNER=sonar-scanner-${SONAR_VERSION}

RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y \
    curl \
    git \
    nodejs \
    npm \
    golang \
    shellcheck \
    unzip
#RUN apk add --no-cache --update nodejs curl git npm go
#RUN apk add --no-cache shellcheck --repository=http://dl-cdn.alpinelinux.org/alpine/edge/community
RUN npm install -g typescript
COPY --from=build /app/drone-sonar /bin/drone-sonar
WORKDIR /bin

RUN curl https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/${SONAR_SCANNER_CLI}.zip -so /bin/${SONAR_SCANNER_CLI}.zip
RUN unzip ${SONAR_SCANNER_CLI}.zip \
    && rm ${SONAR_SCANNER_CLI}.zip

ENV PATH $PATH:/bin/${SONAR_SCANNER}/bin

ENTRYPOINT ["/bin/drone-sonar"]
