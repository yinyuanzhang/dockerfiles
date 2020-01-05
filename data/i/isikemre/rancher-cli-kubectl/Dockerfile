FROM rancher/cli2:v2.2.0
LABEL maintainer="e.isik27@gmail.com"

# Dependencies
RUN apk add --no-cache curl ca-certificates

# Install kubectl
# Note: Latest version may be found on:
# https://aur.archlinux.org/packages/kubectl-bin/
RUN curl https://storage.googleapis.com/kubernetes-release/release/v1.16.2/bin/linux/amd64/kubectl -o /usr/local/bin/kubectl -s

# Custom Entrypoint
COPY entrypoint.sh /

ENV HOME=/config

RUN set -x && \
    chmod +x /entrypoint.sh && \
    chmod +x /usr/local/bin/kubectl && \
    \
    # Basic check it works.
    kubectl version --client

ENTRYPOINT ["/entrypoint.sh"]
