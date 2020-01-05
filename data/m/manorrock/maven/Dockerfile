FROM manorrock/zulu
ENV MAVEN_VERSION 3.6.3
RUN apt-get update && \
    apt-get install -y curl tar && \
    cd /usr/local && \
    curl -O http://mirror.reverse.net/pub/apache/maven/maven-3/${MAVEN_VERSION}/binaries/apache-maven-${MAVEN_VERSION}-bin.tar.gz && \
    tar xfvz apache-maven-${MAVEN_VERSION}-bin.tar.gz && \
    mv apache-maven-${MAVEN_VERSION} maven${MAVEN_VERSION} && \
    rm apache-maven-${MAVEN_VERSION}-bin.tar.gz && \
    rm -rf /var/lib/apt/lists/*
ENV PATH=$PATH:/usr/local/maven${MAVEN_VERSION}/bin
WORKDIR /mnt
