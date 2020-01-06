FROM ubuntu:latest

LABEL maintainer="Saeid Akbari <saeid9063@gmail.com>"

ENV DOCKER_VERSION="18.06.0~ce~3-0~ubuntu"
ENV KUBE_LATEST_VERSION="v1.12.2"
ENV MBT_LATEST_VERSION="0.21.0"

# Install common require tools
RUN apt update
RUN apt install -y curl apt-transport-https ca-certificates software-properties-common libssl1.0.0 git make

# Add docker PPA repository
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
RUN add-apt-repository -y \
    "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
    $(lsb_release -cs) \
    stable"

# Install docker.
RUN apt update && apt install -y docker-ce=${DOCKER_VERSION}

# Install Helm
RUN curl https://raw.githubusercontent.com/helm/helm/master/scripts/get > get_helm.sh \
    && chmod 700 get_helm.sh \
    && ./get_helm.sh

# Installing mbt as monorepo change discovery tool
RUN curl \
    -L -o /usr/local/bin/mbt \
    https://bintray.com/buddyspike/bin/download_file?file_path=mbt_linux_x86_64%2F${MBT_LATEST_VERSION}%2F${MBT_LATEST_VERSION}%2Fmbt_linux_x86_64 \
    && chmod +x /usr/local/bin/mbt

# Delete cache
RUN apt clean --dry-run
