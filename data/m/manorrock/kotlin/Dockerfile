FROM manorrock/openjdk
ENV KOTLIN_VERSION 1.3.61
RUN apt-get update && \
    apt-get install -y curl unzip && \
    cd /usr/local && \
    curl -L -O https://github.com/JetBrains/kotlin/releases/download/v${KOTLIN_VERSION}/kotlin-compiler-${KOTLIN_VERSION}.zip && \
    unzip kotlin-compiler-${KOTLIN_VERSION}.zip && \
    mv kotlinc kotlin${KOTLIN_VERSION} && \
    rm kotlin-compiler-${KOTLIN_VERSION}.zip && \
    apt-get remove -y curl unzip
ENV PATH=$PATH:/usr/local/kotlin${KOTLIN_VERSION}/bin
WORKDIR /mnt

