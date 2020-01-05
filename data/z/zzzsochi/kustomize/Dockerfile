FROM alpine
LABEL maintainer="Alexander Zelenyak <zzz.sochi@gmail.com>"

ARG VERSION=2.0.3

ADD https://github.com/kubernetes-sigs/kustomize/releases/download/v${VERSION}/kustomize_${VERSION}_linux_amd64 /usr/local/bin/kustomize
RUN chmod +x /usr/local/bin/kustomize

ENTRYPOINT ["/usr/local/bin/kustomize"]
