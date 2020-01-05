FROM ubuntu:latest
MAINTAINER Philipp Goellner <philipp.goellner@xaltbc.de>

ENV ANSIBLE_HOST_KEY_CHECKING=false \
    BAMBOO_AGENT_HOME=/var/atlassian/bamboo-agent \
    BAMBOO_AGENT_TIMEOUT=90 \
    BAMBOO_SERVER=false \
    RAM_MIN=256 \
    RAM_MAX=512 \
    DEBIAN_FRONTEND=noninteractive \
    GOROOT=/usr/local/go \
    GO_VERSION=1.13.3 \
    GRADLE_VERSION=2.5 \
    JAVA_HOME=/opt/jdk/jdk1.8.0_212 \
    JAVA8_HOME=/opt/jdk/jdk1.8.0_212 \
    LANG=C.UTF-8 \
    TERRAFORM_VERSION=0.11.8 \
    TIME_ZONE=false \
    IMPORTCERT=false
ENV PATH=${PATH}:/opt/gradle-${GRADLE_VERSION}/bin:${GOROOT}/bin

# ------ Basic modules ------
RUN dpkg --add-architecture i386 \
    && apt-get update \
    && apt-get install --quiet -y   ant \
                                    apt-transport-https \
                                    apt-utils \
                                    build-essential \
                                    curl \
                                    git \
                                    gnupg \
                                    hugo \
                                    jq \
                                    lib32stdc++6 \
                                    lib32gcc1 \
                                    lib32ncurses5 \
                                    lib32z1 \
                                    libc6-i386 \
                                    libjpeg8-dev \
                                    libtcnative-1 \
                                    lsb-release \
                                    pandoc \
                                    python-dev \
                                    python-pip \
                                    python3 \
                                    python3-pip \
                                    rsync \
                                    software-properties-common \
                                    sed \
                                    ssh \
                                    tzdata \
                                    unzip \
                                    wget \
                                    xmlstarlet \
                                    zlib1g-dev \
    && pip install --upgrade        awscli \
                                    Pillow \
    && pip3 install                 mws \
                                    numpy \
                                    PyMySQL \
                                    route53 \
                                    requests \
                                    botocore \
                                    boto \
                                    boto3


# Install Atlassian SDK, Docker, Java, Docker-Compose, Hugo, NodeJS, Apache-Maven and Gradle
RUN apt-add-repository ppa:ansible/ansible \
    && curl -fsSL https://packages.atlassian.com/api/gpg/key/public | apt-key add - \
    && add-apt-repository   "deb https://packages.atlassian.com/atlassian-sdk-deb stable contrib" \
    && curl -fsSL           https://download.docker.com/linux/ubuntu/gpg | apt-key add - \
    && add-apt-repository   "deb [arch=amd64] https://download.docker.com/linux/ubuntu xenial stable" \
    && apt-get update \
    && apt-get install -y   ansible \
                            atlassian-plugin-sdk \
                            docker-ce=17.09.1~ce-0~ubuntu \
    && curl -fsSL https://github.com/docker/compose/releases/download/1.16.1/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose \
    && chmod 0755 /usr/local/bin/docker-compose \
    && curl -fsSL https://deb.nodesource.com/setup_8.x | bash - \
    && apt-get install -y nodejs \
    && curl -fsSL http://www-eu.apache.org/dist/maven/maven-3/3.3.9/binaries/apache-maven-3.3.9-bin.tar.gz | tar xvz -C /usr/local \
    && ln -s /usr/local/apache-maven-3.3.9/bin/mvn /usr/bin/mvn \
    && curl -fsSLo /opt/gradle.zip https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-all.zip \
    && unzip /opt/gradle.zip -d /opt \
    && rm /opt/gradle.zip \
    && curl -fsSL https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip > /tmp/terraform.zip \
    && unzip /tmp/terraform.zip -d /usr/local/bin \
    && rm -f /tmp/terraform.zip \
    && chmod +x /usr/local/bin/terraform \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
    
COPY jdk-8u212-linux-x64.tar.gz 	     .
RUN mkdir /opt/jdk
RUN tar -zxf jdk-8u212-linux-x64.tar.gz -C /opt/jdk
RUN ls /opt/jdk
RUN update-alternatives --install /usr/bin/java java /opt/jdk/jdk1.8.0_212/bin/java 100
RUN update-alternatives --install /usr/bin/javac javac /opt/jdk/jdk1.8.0_212/bin/javac 100
RUN update-alternatives --display java
RUN update-alternatives --display javac
RUN curl -sL https://ibm.biz/idt-installer | bash

RUN curl -fsSL https://dl.google.com/go/go${GO_VERSION}.linux-amd64.tar.gz | tar xvz -C /usr/local

ADD configure-and-start-root.sh   /

VOLUME "${BAMBOO_AGENT_HOME}" \
       "/root/.aws"

ENTRYPOINT ["/configure-and-start-root.sh"]
