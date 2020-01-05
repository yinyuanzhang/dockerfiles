FROM alpine:3.8
ENV KUSTOMIZE_VERSION=3.3.0

WORKDIR /app

RUN apk add --no-cache \
      curl \
      wget \
      git

RUN curl -s https://api.github.com/repos/kubernetes-sigs/kustomize/releases |\
  grep browser_download |\
  grep linux |\
  cut -d '"' -f 4 |\
  grep /kustomize/v${KUSTOMIZE_VERSION} |\
  sort | tail -n 1 |\
  xargs curl -L -O \
  && tar -xzf kustomize_v${KUSTOMIZE_VERSION}_linux_amd64.tar.gz \
  && mv kustomize /usr/local/bin \
  && rm kustomize_v${KUSTOMIZE_VERSION}_linux_amd64.tar.gz

ENTRYPOINT ["kustomize", "build"]