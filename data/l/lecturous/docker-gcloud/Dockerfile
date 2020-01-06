FROM node:boron

RUN apt-get update && apt-get install -y --no-install-recommends apt-transport-https software-properties-common; \
    export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)"; \
    echo "deb https://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list; \
    curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -; \
    curl -fsSL https://apt.dockerproject.org/gpg | apt-key add -; \
    add-apt-repository "deb https://apt.dockerproject.org/repo/ debian-$(lsb_release -cs) main"; \
    apt-get update && apt-get install -y --no-install-recommends docker-engine google-cloud-sdk


