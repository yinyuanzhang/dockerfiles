FROM manorrock/debian
RUN apt-get update && \
    apt-get install -y curl tar gzip && \
    cd /usr/local && \
    curl -L -O https://github.com/AdoptOpenJDK/openjdk13-binaries/releases/download/jdk-13.0.1%2B9/OpenJDK13U-jdk_x64_linux_hotspot_13.0.1_9.tar.gz && \
    tar xfvz OpenJDK13U-jdk_x64_linux_hotspot_13.0.1_9.tar.gz && \
    rm OpenJDK13U-jdk_x64_linux_hotspot_13.0.1_9.tar.gz && \
    mv jdk-13.0.1+9 adoptopenjdk13.0.1 && \
    rm -rf /var/lib/apt/lists/*
ENV PATH=$PATH:/usr/local/adoptopenjdk13.0.1/bin
WORKDIR /mnt

