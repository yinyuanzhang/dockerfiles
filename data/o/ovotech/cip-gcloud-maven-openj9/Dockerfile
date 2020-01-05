FROM docker:18.03.1-ce as static-docker-source

FROM adoptopenjdk/maven-openjdk11-openj9

COPY --from=static-docker-source /usr/local/bin/docker /usr/local/bin/docker

ARG CLOUD_SDK_VERSION=219.0.1
ENV CLOUD_SDK_VERSION=$CLOUD_SDK_VERSION

RUN apt-get update -qqy && apt-get install -qqy \
        curl \
        gcc \
        python-dev \
        python-setuptools \
        apt-transport-https \
        lsb-release \
        openssh-client \
        git \
        gnupg \
    && python /usr/lib/python2.7/dist-packages/easy_install.py -U pip && \
    pip install -U crcmod && \
    export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)" && \
    echo "deb https://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" > /etc/apt/sources.list.d/google-cloud-sdk.list && \
    curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - && \
    apt-get update && apt-get install -y google-cloud-sdk=${CLOUD_SDK_VERSION}-0 kubectl && \
    gcloud config set core/disable_usage_reporting true && \
    gcloud config set component_manager/disable_update_check true && \
    gcloud config set metrics/environment github_docker_image && \
    gcloud --version && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    mkdir /.ssh
VOLUME ["/root/.config"]
VOLUME ["/.config"]
CMD ["/bin/bash"]