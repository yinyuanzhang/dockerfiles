FROM docker:stable
ENV KUBECTL_VERSION="1.8.7" \
    YQ_VERSION="1.14.0" \ 
    PATH=/opt/kubernetes-deploy:$PATH

# Install pre-req
RUN apk add -U openssl curl tar gzip bash ca-certificates git wget jq libintl coreutils \
   && apk add --virtual build_deps gettext \
   && mv /usr/bin/envsubst /usr/local/bin/envsubst \
   && apk del build_deps

# Install deploy scripts
COPY / /opt/kubernetes-deploy/

RUN wget -q -O /usr/local/bin/clair-scanner https://github.com/arminc/clair-scanner/releases/download/v8/clair-scanner_linux_amd64 && chmod +x /usr/local/bin/clair-scanner

# Install yq
RUN wget -q -O /usr/local/bin/yq https://github.com/mikefarah/yq/releases/download/$YQ_VERSION/yq_linux_amd64 && chmod +x /usr/local/bin/yq

# Install kubectl
RUN curl -L -o /usr/bin/kubectl https://storage.googleapis.com/kubernetes-release/release/v$KUBECTL_VERSION/bin/linux/amd64/kubectl \
    && chmod +x /usr/bin/kubectl \
    && kubectl version --client
