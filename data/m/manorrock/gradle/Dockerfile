FROM manorrock/openjdk
ENV GRADLE_VERSION 6.0.1
RUN apt-get update && \
    apt-get install -y curl unzip && \
    cd /usr/local && \
    curl -L -O https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip && \
    unzip gradle-${GRADLE_VERSION}-bin.zip && \
    mv gradle-${GRADLE_VERSION} gradle${GRADLE_VERSION} && \
    rm gradle-${GRADLE_VERSION}-bin.zip && \
    rm -rf /var/lib/apt/lists/* 
ENV PATH=$PATH:/usr/local/gradle${GRADLE_VERSION}/bin
WORKDIR /mnt
