FROM centos:latest

LABEL maintainer="Federico Lelli"

# Tool version variables
ENV JDK_VERSION 11
ENV GRADLE_VERSION 5.1
ENV HUGO_VERSION 0.53
ENV HELM_VERSION 2.12.3
ENV DRAFT_VERSION 0.16.0
ENV SKAFFOLD_VERSION 0.22.0
ENV TERRAFORM_VERSION 0.11.11

# Optional arguments that can be overridden at build time
ARG BUILD_DATE
ARG VCS_REF
ARG VERSION

# These variables are used by Terraform to authenticate to GitHub, GitLab and Netlify with user credentials
# There is no default value as they have to be passed at container creation.
#ENV GITHUB_TOKEN
#ENV GITLAB_TOKEN
#ENV NETLIFY_TOKEN

# Labels in the custom namespace
LABEL com.mooltiverse.service.description="Operations tools used at Mooltiverse" \
      com.mooltiverse.service.product.name="ops-centos" \
      com.mooltiverse.service.product.version="${VERSION}" \
      com.mooltiverse.service.product.flavor="centos" \
      com.mooltiverse.service.product.url="https://github.com/mooltiverse/tools" \
      com.mooltiverse.service.product.vendor.name="Mooltiverse" \
      com.mooltiverse.service.product.vendor.url="https://www.mooltiverse.com/"

# Labels according to the Label Schema Convention (http://label-schema.org/)
LABEL org.label-schema.schema-version="1.0" \
      org.label-schema.build-date="${BUILD_DATE}" \
      org.label-schema.name="ops-centos" \
      org.label-schema.description="Operations tools used at Mooltiverse" \
      org.label-schema.usage="https://github.com/mooltiverse/tools" \
      org.label-schema.url="https://github.com/mooltiverse/tools" \
      org.label-schema.vcs-url="https://github.com/mooltiverse/tools" \
      org.label-schema.vcs-ref="${VCS_REF}" \
      org.label-schema.vendor="Mooltiverse" \
      org.label-schema.version="${VERSION}" \
      org.label-schema.docker.cmd="docker run -v ~:/home/user -v /mnt/data:/mnt/data /bin/bash"

# Install base packages and set locales
RUN \
    yum -y install \
            curl \
            device-mapper-persistent-data \
            gcc-c++ \
            git \
            gnupg2 \
            make \
            mc \
            sudo \
            wget \
            which \
            yum-utils \
            zip unzip && \
    localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8
ENV LANG en_US.utf8

# Create users and groups
RUN useradd -c "Docker default user" -b /home/user -d /home/user -u 1000 -m -s /bin/bash user
# Add the user to the wheel group to give it the sudo privilege (enabled by default in /etc/sudoers)
RUN usermod -aG wheel user
# Add a new file in /etc/sudoers.d to allow the user not only to be a sudoer
# (as it belongs to the wheel group) but also to do sudo with no password
# and preserve the environment when using 'sudo -E'
RUN echo "user ALL=(ALL:ALL) SETENV: NOPASSWD: ALL" >> /etc/sudoers.d/user

# Comment out some defaults from /etc/sudoers so that the user can sudo preserving
# the environment (when running sudo with the -E flag), including the HOME variable
RUN cp /etc/sudoers /etc/sudoers.orig && \
    sed -i 's/^Defaults    always_set_home/#Defaults    always_set_home/g' /etc/sudoers && \
    sed -i 's/^Defaults    env_reset/#Defaults    env_reset/g' /etc/sudoers && \
    sed -i 's/^Defaults    secure_path/#Defaults    secure_path/g' /etc/sudoers

# Create additional directories in the user home and set access control
RUN mkdir -p /home/user/.config && chown user.user /home/user/.config

# Install Python3
RUN \
    yum -y install https://centos7.iuscommunity.org/ius-release.rpm && \
    yum -y update && \
    yum -y install python36u python36u-libs python36u-devel python36u-pip

# Install Open JDK
RUN \
    yum -y install java-${JDK_VERSION}-openjdk
ENV JAVA_HOME /usr/lib/jvm/jre-${JDK_VERSION}-openjdk

# Install Docker
# Remember that running Docker inside the containers requires the host's socket
# to be shared with the container. Do so by passing:
#       -v /var/run/docker.sock:/var/run/docker.sock
RUN \
    yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo && \
    yum install -y docker-ce docker-ce-cli containerd.io && \
    usermod -aG docker user

# Install Docker Compose
RUN \
    curl -L "https://github.com/docker/compose/releases/download/1.23.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose && \
    chmod +x /usr/local/bin/docker-compose

# Install the Google Cloud SDK
RUN echo "[google-cloud-sdk]" >> /etc/yum.repos.d/google-cloud-sdk.repo && \
    echo "name=Google Cloud SDK" >> /etc/yum.repos.d/google-cloud-sdk.repo && \
    echo "baseurl=https://packages.cloud.google.com/yum/repos/cloud-sdk-el7-x86_64" >> /etc/yum.repos.d/google-cloud-sdk.repo && \
    echo "enabled=1" >> /etc/yum.repos.d/google-cloud-sdk.repo && \
    echo "gpgcheck=1" >> /etc/yum.repos.d/google-cloud-sdk.repo && \
    echo "repo_gpgcheck=1" >> /etc/yum.repos.d/google-cloud-sdk.repo && \
    echo "gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg" >> /etc/yum.repos.d/google-cloud-sdk.repo && \
    echo "       https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg" >> /etc/yum.repos.d/google-cloud-sdk.repo && \
    yum install -y google-cloud-sdk

# Install Kubernetes tools
RUN echo "[kubernetes]" >> /etc/yum.repos.d/kubernetes.repo && \
    echo "name=Kubernetes" >> /etc/yum.repos.d/kubernetes.repo && \
    echo "baseurl=https://packages.cloud.google.com/yum/repos/kubernetes-el7-x86_64" >> /etc/yum.repos.d/kubernetes.repo && \
    echo "enabled=1" >> /etc/yum.repos.d/kubernetes.repo && \
    echo "gpgcheck=1" >> /etc/yum.repos.d/kubernetes.repo && \
    echo "repo_gpgcheck=1" >> /etc/yum.repos.d/kubernetes.repo && \
    echo "gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg" >> /etc/yum.repos.d/kubernetes.repo && \
    echo "       https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg" >> /etc/yum.repos.d/kubernetes.repo && \
    yum install -y kubeadm kubectl kubelet

# Install the AWS CLI using the bundled installer
RUN \
    mkdir -p /opt/awscli && \
    cd /opt/awscli && wget -q https://s3.amazonaws.com/aws-cli/awscli-bundle.zip && \
    cd /opt/awscli && unzip awscli-bundle.zip && \
    /opt/awscli/awscli-bundle/install -i /opt/awscli/current && \
    ln -s /opt/awscli/current /opt/awscli/latest && \
    rm -rf /opt/awscli/awscli-bundle.zip /opt/awscli/awscli-bundle && \
    /opt/awscli/current/bin/aws --version
ENV AWS_HOME /opt/awscli/current

# Install the Azure CLI
RUN \
    rpm --import https://packages.microsoft.com/keys/microsoft.asc && \
    sh -c 'echo -e "[azure-cli]\nname=Azure CLI\nbaseurl=https://packages.microsoft.com/yumrepos/azure-cli\nenabled=1\ngpgcheck=1\ngpgkey=https://packages.microsoft.com/keys/microsoft.asc" > /etc/yum.repos.d/azure-cli.repo' && \
    sudo yum install -y azure-cli

# Install Gradle
RUN \
    mkdir -p /opt/gradle/ && \
    cd /opt/gradle && wget -q https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip && \
    cd /opt/gradle && unzip -q /opt/gradle/gradle-${GRADLE_VERSION}-bin.zip -d /opt/gradle/ && \
    rm -f /opt/gradle/gradle-${GRADLE_VERSION}-bin.zip && \
    ln -s /opt/gradle/gradle-${GRADLE_VERSION} /opt/gradle/current && \
    ln -s /opt/gradle/gradle-${GRADLE_VERSION} /opt/gradle/latest
ENV GRADLE_HOME /opt/gradle/current

# Install Hugo
RUN \
    mkdir -p /opt/hugo/hugo-${HUGO_VERSION} && \
    cd /opt/hugo/hugo-${HUGO_VERSION} && wget -q https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_${HUGO_VERSION}_Linux-64bit.tar.gz && \
    cd /opt/hugo/hugo-${HUGO_VERSION} && tar -xzf hugo_${HUGO_VERSION}_Linux-64bit.tar.gz && \
    chmod ugo+x /opt/hugo/hugo-${HUGO_VERSION}/hugo && \
    rm -f /opt/hugo/hugo-${HUGO_VERSION}/hugo_${HUGO_VERSION}_Linux-64bit.tar.gz && \
    ln -s /opt/hugo/hugo-${HUGO_VERSION} /opt/hugo/current && \
    ln -s /opt/hugo/hugo-${HUGO_VERSION} /opt/hugo/latest
ENV HUGO_HOME /opt/hugo/current
EXPOSE 1313

# Install Helm
RUN \
    mkdir -p /opt/helm/helm-${HELM_VERSION} && \
    cd /opt/helm/helm-${HELM_VERSION} && wget -q https://storage.googleapis.com/kubernetes-helm/helm-v${HELM_VERSION}-linux-amd64.tar.gz && \
    cd /opt/helm/helm-${HELM_VERSION} && tar -xzf helm-v${HELM_VERSION}-linux-amd64.tar.gz && \
    rm -f /opt/helm/helm-${HELM_VERSION}/helm-v${HELM_VERSION}-linux-amd64.tar.gz && \
    ln -s /opt/helm/helm-${HELM_VERSION} /opt/helm/current && \
    ln -s /opt/helm/helm-${HELM_VERSION} /opt/helm/latest
ENV HELM_PATH /opt/helm/current/linux-amd64

# Install Draft
RUN \
    mkdir -p /opt/draft/draft-${DRAFT_VERSION} && \
    cd /opt/draft/draft-${DRAFT_VERSION} && wget -q https://azuredraft.blob.core.windows.net/draft/draft-v${DRAFT_VERSION}-linux-amd64.tar.gz && \
    cd /opt/draft/draft-${DRAFT_VERSION} && tar -xzf draft-v${DRAFT_VERSION}-linux-amd64.tar.gz && \
    rm -f /opt/draft/draft-${DRAFT_VERSION}/draft-v${DRAFT_VERSION}-linux-amd64.tar.gz && \
    ln -s /opt/draft/draft-${DRAFT_VERSION} /opt/draft/current && \
    ln -s /opt/draft/draft-${DRAFT_VERSION} /opt/draft/latest
ENV DRAFT_PATH /opt/draft/current/linux-amd64

# Install Skaffold
RUN \
    mkdir -p /opt/skaffold/skaffold-${SKAFFOLD_VERSION} && \
    cd /opt/skaffold/skaffold-${SKAFFOLD_VERSION} && curl -Lo skaffold https://storage.googleapis.com/skaffold/releases/v${SKAFFOLD_VERSION}/skaffold-linux-amd64 && \
    cd /opt/skaffold/skaffold-${SKAFFOLD_VERSION} && chmod +x skaffold && \
    ln -s /opt/skaffold/skaffold-${SKAFFOLD_VERSION} /opt/skaffold/current && \
    ln -s /opt/skaffold/skaffold-${SKAFFOLD_VERSION} /opt/skaffold/latest
ENV SKAFFOLD_PATH /opt/skaffold/current

# Install Terraform
RUN \
    mkdir -p /opt/terraform/terraform-${TERRAFORM_VERSION} && \
    cd /opt/terraform && wget -q https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip && \
    cd /opt/terraform && unzip -q /opt/terraform/terraform_${TERRAFORM_VERSION}_linux_amd64.zip -d /opt/terraform/terraform-${TERRAFORM_VERSION}/ && \
    rm -f /opt/terraform/terraform_${TERRAFORM_VERSION}_linux_amd64.zip && \
    ln -s /opt/terraform/terraform-${TERRAFORM_VERSION} /opt/terraform/current && \
    ln -s /opt/terraform/terraform-${TERRAFORM_VERSION} /opt/terraform/latest
ENV TERRAFORM_HOME /opt/terraform/current

# Install Node.js and npm
RUN \
    curl --silent --location https://rpm.nodesource.com/setup_10.x | bash - && \
    yum -y install nodejs

# Set the PATH env variable
ENV PATH $PATH:$JAVA_HOME/bin:$AWS_HOME/bin:$GRADLE_HOME/bin:$HUGO_HOME:$TERRAFORM_HOME:$HELM_PATH:$DRAFT_PATH:$SKAFFOLD_PATH

# Persistent volumes:
# - /home/user is used to mount the home directory, where all of the settings and credentials are stored
# - /mnt/data is used to mount the development folder
VOLUME /home/user
VOLUME /mnt/data

# Set the process working dir
WORKDIR /mnt/data

# The user the image is ran with
USER user

# If no command is provided, just wait indefinitely so that the container can be
# created and then started and stay active until stopped
CMD exec /bin/bash -c "trap : TERM INT; sleep infinity & wait"
