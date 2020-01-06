# TODO: We should have a job that creates a S4TF base image so that
#we don't have to duplicate the installation everywhere.
FROM nvidia/cuda:10.0-cudnn7-devel-ubuntu18.04

# Allows the caller to specify the toolchain to use.
ARG swift_tf_url=https://storage.googleapis.com/s4tf-kokoro-artifact-testing/latest/swift-tensorflow-DEVELOPMENT-cuda10.0-cudnn7-ubuntu18.04.tar.gz
ARG swift_url=https://swift.org/builds/development/ubuntu1804/swift-DEVELOPMENT-SNAPSHOT-2019-03-17-a/swift-DEVELOPMENT-SNAPSHOT-2019-03-17-a-ubuntu18.04.tar.gz

# Install Swift deps.
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        ca-certificates \
        curl \
	openssl \
	net-tools \
        git \
        python \
        clang \
        libbsd-dev \
        libcurl4-openssl-dev \
        libicu-dev \
        libncurses5-dev \
        libxml2 \
        libblocksruntime-dev \
	libpython3.6-dev \
	libsqlite3-dev

# Download and extract S4TF
WORKDIR /swift-tensorflow-toolchain
RUN curl -fSsL $swift_tf_url -o swift.tar.gz \
    && mkdir usr \
    && tar -xzf swift.tar.gz --directory=usr --strip-components=1 \
    && rm swift.tar.gz

WORKDIR /swift-toolchain
RUN curl -fSsL $swift_url -o swift.tar.gz \
    && mkdir usr \
    && tar -xzf swift.tar.gz --directory=usr --strip-components=1 \
    && rm swift.tar.gz

# Copy the kernel into the container
WORKDIR /swift-apis
COPY . .

# Configure cuda
RUN echo "/usr/local/cuda-10.0/targets/x86_64-linux/lib/stubs" > /etc/ld.so.conf.d/cuda-10.0-stubs.conf && \
    ldconfig

ENV SOURCEKIT_TOOLCHAIN_PATH=/swift-tensorflow-toolchain
ENV PATH="/swift-tensorflow-toolchain/usr/bin:${PATH}"

WORKDIR /temp

RUN git clone https://github.com/apple/sourcekit-lsp.git && cd sourcekit-lsp && \
    swift package update && swift build -Xcxx -I/$SOURCEKIT_TOOLCHAIN_PATH/usr/lib/swift && \
    mv .build/debug/sourcekit-lsp /usr/local/bin

ENV CODE_VERSION=1.408-vsc1.32.0
RUN curl -fSsL https://github.com/codercom/code-server/releases/download/$CODE_VERSION/code-server$CODE_VERSION-linux-x64.tar.gz -o code-server.tar.gz && \
    tar xvzf code-server.tar.gz && \
    cp code-server$CODE_VERSION-linux-x64/code-server /usr/bin/
EXPOSE 8443
ENTRYPOINT ["code-server"]
