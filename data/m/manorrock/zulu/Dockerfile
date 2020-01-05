FROM manorrock/debian
RUN apt-get update && \
    apt-get install -y curl tar gzip && \
    cd /usr/local && \
    curl --insecure -L -O https://cdn.azul.com/zulu/bin/zulu13.28.11-ca-jdk13.0.1-linux_x64.tar.gz && \
    tar xfvz zulu13.28.11-ca-jdk13.0.1-linux_x64.tar.gz && \
    mv zulu13.28.11-ca-jdk13.0.1-linux_x64 zulu13.0.1 && \
    rm zulu13.28.11-ca-jdk13.0.1-linux_x64.tar.gz && \
    rm -rf /var/lib/apt/lists/* 
ENV PATH=$PATH:/usr/local/zulu13.0.1/bin
WORKDIR /mnt
