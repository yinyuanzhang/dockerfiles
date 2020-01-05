FROM manorrock/debian
ENV GRAALVM_VERSION 19.3.0.2
RUN apt-get update && \
    apt-get install -y curl tar gzip && \
    cd /usr/local && \
    curl -L -O https://github.com/graalvm/graalvm-ce-builds/releases/download/vm-${GRAALVM_VERSION}/graalvm-ce-java11-linux-amd64-${GRAALVM_VERSION}.tar.gz && \
    tar xfvz graalvm-ce-java11-linux-amd64-${GRAALVM_VERSION}.tar.gz && \
    mv graalvm-ce-java11-${GRAALVM_VERSION} graalvm-java11-${GRAALVM_VERSION} && \
    rm graalvm-ce-java11-linux-amd64-${GRAALVM_VERSION}.tar.gz && \
    rm -rf /var/lib/apt/lists/* 
ENV PATH=$PATH:/usr/local/graalvm-java11-${GRAALVM_VERSION}/bin
RUN gu install native-image
WORKDIR /mnt
