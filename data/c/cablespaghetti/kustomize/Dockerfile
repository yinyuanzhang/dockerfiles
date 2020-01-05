FROM alpine:3.8
ENV KUSTOMIZE_VER 1.0.4
ENV KUBECTL_VER 1.11.1
ENV HEPTIO_VER 0.3.0

RUN apk --no-cache add curl gettext bash

RUN mkdir /working
WORKDIR /working

RUN curl -L https://github.com/kubernetes-sigs/kustomize/releases/download/v${KUSTOMIZE_VER}/kustomize_${KUSTOMIZE_VER}_linux_amd64  -o /usr/bin/kustomize \
    && chmod +x /usr/bin/kustomize

RUN curl -L https://storage.googleapis.com/kubernetes-release/release/v${KUBECTL_VER}/bin/linux/amd64/kubectl -o /usr/bin/kubectl \
    && chmod +x /usr/bin/kubectl

RUN curl -L https://github.com/kubernetes-sigs/aws-iam-authenticator/releases/download/v${HEPTIO_VER}/heptio-authenticator-aws_${HEPTIO_VER}_linux_amd64 \
    -o /usr/bin/heptio-authenticator-aws && chmod +x /usr/bin/heptio-authenticator-aws

CMD ["/usr/bin/kustomize"]
