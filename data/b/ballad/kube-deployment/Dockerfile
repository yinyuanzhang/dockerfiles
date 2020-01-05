FROM node:8.15.1-alpine

ENV KUBECTL_VERSION="v1.13.4"

ENV HELM_VERSION="v2.13.0"

RUN apk add --update ca-certificates bash gnupg jq py-pip wget git \
  && apk add --update -t deps curl gettext \
  && pip install awscli \
  && rm -rf /var/cache/apk/*

RUN curl -L https://storage.googleapis.com/kubernetes-release/release/${KUBECTL_VERSION}/bin/linux/amd64/kubectl -o /usr/local/bin/kubectl \
  & curl -L https://github.com/kubernetes-sigs/aws-iam-authenticator/releases/download/v0.3.0/heptio-authenticator-aws_0.3.0_linux_amd64 -o /usr/local/bin/aws-iam-authenticator \
  & wait \
  && chmod +x /usr/local/bin/kubectl \
  && chmod +x /usr/local/bin/aws-iam-authenticator \
  && wget -q https://storage.googleapis.com/kubernetes-helm/helm-${HELM_VERSION}-linux-amd64.tar.gz -O - | tar -xzO linux-amd64/helm > /usr/local/bin/helm \
  && chmod +x /usr/local/bin/helm


# Install Helm plugins
RUN helm init --client-only
RUN helm plugin install https://github.com/viglesiasce/helm-gcs.git
RUN helm plugin install https://github.com/databus23/helm-diff
RUN helm plugin install https://github.com/chartmuseum/helm-push


RUN curl -L https://github.com/Praqma/helmsman/releases/download/v1.7.4/helmsman_1.7.4_linux_amd64.tar.gz | tar zx \
 && mv helmsman /usr/local/bin/helmsman \
 && chmod +x /usr/local/bin/helmsman

RUN npm install -g simple-scaffold
