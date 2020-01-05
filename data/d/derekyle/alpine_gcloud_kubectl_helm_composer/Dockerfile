FROM docker:latest

ARG HELM_VERSION="v2.14.2"
ARG CLOUD_SDK_VERSION=255.0.0


ENV CLOUD_SDK_VERSION=$CLOUD_SDK_VERSION
ENV HELM_VERSION=$HELM_VERSION


ENV PATH /google-cloud-sdk/bin:$PATH
RUN apk --no-cache add \
        make \
        bash \
        ca-certificates \
        curl \
        gnupg \
        python \
        py-crcmod \
        libc6-compat \
        openssh-client \
        php \
        php-curl \
        php-openssl \
        php-json \
        php-phar \
        php-dom \
        php-iconv \
    && curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz && \
    tar xzf google-cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz && \
    rm google-cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz && \
    ln -s /lib /lib64 && \
    gcloud config set core/disable_usage_reporting true && \
    gcloud config set component_manager/disable_update_check true && \
    gcloud config set metrics/environment github_docker_image && \
    gcloud --version && \
    gcloud components install kubectl \
    && wget -q https://storage.googleapis.com/kubernetes-helm/helm-${HELM_VERSION}-linux-amd64.tar.gz -O - | tar -xzO linux-amd64/helm > /usr/local/bin/helm \
    && chmod +x /usr/local/bin/helm \
    && curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin --filename=composer
