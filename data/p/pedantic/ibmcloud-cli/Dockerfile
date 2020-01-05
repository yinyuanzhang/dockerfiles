FROM alpine:3.10

ENV PATH=/opt/IBM_Cloud_CLI/:$PATH
SHELL ["/bin/ash", "-eo", "pipefail", "-c"]

RUN apk add --no-cache \
    bash \
    bc \
    curl \
    docker \
    git \
    jq \
    openssl \
    stow \
    vim

# Change shell to bash
RUN sed -i '/^root:/ s/\/ash$/\/bash$/' /etc/passwd

# Install helm
RUN curl https://raw.githubusercontent.com/kubernetes/helm/master/scripts/get > /tmp/get_helm.sh \
    && chmod 700 /tmp/get_helm.sh \
    && /tmp/get_helm.sh \
    && rm /tmp/get_helm.sh

# Install container
RUN mkdir -p /opt && curl -L https://clis.ng.bluemix.net/download/bluemix-cli/latest/linux64/archive | tar -xz -C /opt/ \
    && ibmcloud plugin install container-service \
    && ibmcloud plugin install container-registry

# Install kubectl
RUN curl -L https://storage.googleapis.com/kubernetes-release/release/"$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)"/bin/linux/amd64/kubectl -o /opt/IBM_Cloud_CLI/kubectl \
    && chmod a+x /opt/IBM_Cloud_CLI/kubectl

# Install calicoctl

RUN curl -s https://api.github.com/repos/projectcalico/calicoctl/releases/latest | \
    jq '[.assets[]|{key: .name|sub("calicoctl-";"")|sub(".exe";""), value:.browser_download_url}] | from_entries' | \
    jq '."linux-amd64"' | \
    xargs curl -L -o /usr/bin/calicoctl \
    && chmod a+x /usr/bin/calicoctl

WORKDIR /root
