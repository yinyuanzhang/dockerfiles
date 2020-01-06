FROM alpine:3


ENV HELM_VERSION=v3.0.2
ENV HELMFILE_VERSION=v0.98.1
ENV AWSCLI_VERSION=1.16.309
ENV KUBECTL_VERSION=v1.16.2

ENV BASE_URL="https://get.helm.sh"
ENV TAR_FILE="helm-${HELM_VERSION}-linux-amd64.tar.gz"

RUN apk --update add git less openssh curl ca-certificates python python-dev py-pip build-base && \
    pip install awscli==${AWSCLI_VERSION} --upgrade --user && \
    curl -L ${BASE_URL}/${TAR_FILE} |tar xvz && \
    curl -L https://github.com/roboll/helmfile/releases/download/${HELMFILE_VERSION}/helmfile_linux_amd64 -O && \
    curl -L https://storage.googleapis.com/kubernetes-release/release/${KUBECTL_VERSION}/bin/linux/amd64/kubectl -O && \
    mv kubectl /usr/bin/kubectl && \
    mv helmfile_linux_amd64 /usr/bin/helmfile && \
    mv linux-amd64/helm /usr/bin/helm && \
    chmod +x /usr/bin/helm && \
    chmod +x /usr/bin/helmfile && \
    chmod +x /usr/bin/kubectl && \
    rm -rf linux-amd64 && \
    apk --purge -v del curl py-pip && \
    rm -f /var/cache/apk/* && \
    helm plugin install https://github.com/belitre/helm-push-artifactory-plugin

#WORKDIR /apps

#ENTRYPOINT ["/bin/bash"]
CMD ["/bin/bash"]
