# https://hub.docker.com/_/golang
FROM golang:1.11-alpine

LABEL maintainer Tom Manville<tom@kasten.io>

RUN apk add --update --no-cache \
        ca-certificates \
        # https://github.com/Masterminds/glide#supported-version-control-systems
        bash curl git libc6-compat \
        openssh make \
 # Add go into busybox path
 && ln -s /usr/local/go/bin/go /bin/go \
 && update-ca-certificates \
    \
 # Install kubectl
 && curl -Lo kubectl https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl \
 && chmod +x kubectl \
 && mv kubectl /bin/kubectl \
 # Download and unpack Glide sources
 && curl -L -o /tmp/glide.tar.gz \
          https://github.com/Masterminds/glide/archive/v0.13.2.tar.gz \
 && tar -xzf /tmp/glide.tar.gz -C /tmp \
 && mkdir -p $GOPATH/src/github.com/Masterminds \
 && mv /tmp/glide-* $GOPATH/src/github.com/Masterminds/glide \
 && cd $GOPATH/src/github.com/Masterminds/glide \
    \
 # Build and install Glide executable
 && make install \
    \
 # Install Glide license
 && mkdir -p /usr/local/share/doc/glide \
 && cp LICENSE /usr/local/share/doc/glide/ \
    \
 && rm -rf /var/cache/apk/* \
           $GOPATH/src/* \
           /tmp/*

COPY --from=goreleaser/goreleaser:v0.101.0 /bin/goreleaser /usr/local/bin/
