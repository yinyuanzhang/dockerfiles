FROM alpine:3.9

ENV KUBE_LATEST_VERSION="v1.13.4"
ENV DOCTL_VERSION="1.14.0"

# initiate workdir
WORKDIR /app

# setup dependencies
RUN apk add --update ca-certificates \
  && apk add --update -t deps curl \
  && mkdir /lib64 \
  && ln -s /lib/libc.musl-x86_64.so.1 /lib64/ld-linux-x86-64.so.2

# install kubectl
RUN curl -L https://storage.googleapis.com/kubernetes-release/release/${KUBE_LATEST_VERSION}/bin/linux/amd64/kubectl -o /usr/local/bin/kubectl \
  && chmod +x /usr/local/bin/kubectl

# install doctl
RUN curl -L https://github.com/digitalocean/doctl/releases/download/v${DOCTL_VERSION}/doctl-${DOCTL_VERSION}-linux-amd64.tar.gz | tar xz \
  && cp doctl /usr/local/bin/doctl \
  && chmod +x /usr/local/bin/doctl

# clean ups
RUN apk del --purge deps \
  && rm /var/cache/apk/*

ENTRYPOINT ["/bin/sh", "-c"]
CMD ["kubectl", "help"]
