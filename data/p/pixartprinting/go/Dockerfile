FROM golang:stretch
LABEL maintainer=it-devops@pixartprinting.com

# Update packages
RUN ln -snf /usr/share/zoneinfo/Europe/Rome /etc/localtime && \
    echo Europe/Rome > /etc/timezone && \
    apt-get update && \
    apt-get install -y \
    ca-certificates

# Install certificate
COPY cert.crt /tmp/cert.crt
RUN cp /tmp/cert.crt /usr/local/share/ca-certificates/ && \
    update-ca-certificates

# Install latest linter version
RUN curl -sfL https://raw.githubusercontent.com/golangci/golangci-lint/master/install.sh | \
    sh -s -- -b $GOPATH/bin `curl --silent "https://api.github.com/repos/golangci/golangci-lint/releases/latest" | \
    grep '"tag_name":' | \
    sed -E 's/.*"([^"]+)".*/\1/'`

WORKDIR /work