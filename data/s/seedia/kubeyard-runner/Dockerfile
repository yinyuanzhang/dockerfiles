FROM docker:18.09.2

RUN apk add --no-cache \
    bash \
    coreutils \
    git \
    python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade --no-cache-dir pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi

ENV KUBE_VERSION="v1.13.4"
ENV HELM_VERSION="v2.13.1"
RUN apk add --no-cache ca-certificates \
    && wget -q https://storage.googleapis.com/kubernetes-release/release/${KUBE_VERSION}/bin/linux/amd64/kubectl -O /usr/local/bin/kubectl \
    && chmod +x /usr/local/bin/kubectl \
    && wget -q https://storage.googleapis.com/kubernetes-helm/helm-${HELM_VERSION}-linux-amd64.tar.gz -O - | tar -xzO linux-amd64/helm > /usr/local/bin/helm \
    && chmod +x /usr/local/bin/helm

ENV CLOUD_SDK_VERSION=234.0.0
ENV PATH /google-cloud-sdk/bin:$PATH
RUN apk --no-cache add \
        curl \
        python \
        py-crcmod \
        bash \
        libc6-compat \
        openssh-client \
        git \
        gnupg \
    && curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz && \
    tar xzf google-cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz && \
    rm google-cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz && \
    ln -s /lib /lib64 && \
    gcloud config set core/disable_usage_reporting true && \
    gcloud config set component_manager/disable_update_check true && \
    gcloud config set metrics/environment github_docker_image && \
    gcloud --version

ENV AZ_VERSION="2.0.67"

RUN apk add --no-cache --virtual=build gcc python3-dev musl-dev libffi-dev openssl-dev make && \
    pip3 install --no-cache-dir azure-cli==${AZ_VERSION} && \
    apk del --purge build && \
    echo 'python3 -m azure.cli "$@"' >  /usr/bin/az

RUN pip --no-cache-dir install git+https://github.com/seediacity/kubeyard@0.5.2seedia4

VOLUME ["/root/.config"]
CMD bash
