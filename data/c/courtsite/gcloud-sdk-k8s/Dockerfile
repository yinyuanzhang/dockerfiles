FROM google/cloud-sdk:257.0.0-alpine

LABEL org.label-schema.vcs-url="https://github.com/courtsite/docker-gcloud-k8s" \
      maintainer="Courtsite <tech@courtsite.my>"

RUN apk add --no-cache curl git jq nano wget

RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/v1.15.0/bin/linux/amd64/kubectl \
        && chmod +x ./kubectl \
        && mv ./kubectl /usr/local/bin/kubectl \
        && kubectl version --client=true
