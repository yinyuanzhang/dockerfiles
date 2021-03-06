# This is the base image for mesosphere/dcos-commons, created in order to
# overcome issues such as DCOS-44265 which come about because neither the 18.04
# tag is immutable, nor the apt-get install command is repeatable.
#
# If you need a new version of this image (either because you require more
# recent versions of the base OS or one of the packages installed here, or
# because you modified this file), there are two ways to use it:
#
# 1) Slower but semi-automatic and public:
# - once the desired version of this file is merged to master, the auto-builder
#   on dockerhub will build a new version of this image
# - at that point, renovatebot will make a PR to bump the sha in FROM line in
#   Dockerfile (of the main image)
#
# 2) Faster, for local testing:
# - make the required changes to this file, and/or run the following build
#   command with --no-cache 
# $ TAG=$(date +%Y%m%d)-local
# $ docker build -f Dockerfile.base -t mesosphere/dcos-commons-base:$TAG .
# - put the tag into the FROM line in Dockerfile (of the main image)
#   temporarily, rebuild that one, test, etc.
#
FROM ubuntu:18.04@sha256:29934af957c53004d7fb6340139880d23fb1952505a15d69a03af0d1418878cb

# Install JDK via PPA: https://github.com/franzwong/til/blob/master/java/silent-install-oracle-jdk8-ubuntu.md
RUN apt-get update && \
    apt-get install -y python3-software-properties software-properties-common && \
    add-apt-repository -y ppa:webupd8team/java && \
    apt-get update && \
    echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 select true" | debconf-set-selections && \
    apt-get install -y \
    curl \
    git \
    jq \
    libssl-dev \
    oracle-java8-installer \
    python-pip \
    python3 \
    python3-dev \
    python3-pip \
    rsync \
    tox \
    software-properties-common \
    upx-ucl \
    wget \
    zip && \
    rm -rf /var/lib/apt/lists/* && \
    java -version
