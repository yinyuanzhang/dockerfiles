FROM manorrock/zulu:arm32v6
ENV GROOVY_VERSION 2.5.7
RUN ["cross-build-start"]
RUN apt-get update && \
    apt-get install curl unzip && \
    cd /usr/local && \
    curl -L -O https://dl.bintray.com/groovy/maven/apache-groovy-binary-${GROOVY_VERSION}.zip && \
    unzip apache-groovy-binary-${GROOVY_VERSION}.zip && \
    mv groovy-${GROOVY_VERSION} groovy${GROOVY_VERSION} && \
    rm apache-groovy-binary-${GROOVY_VERSION}.zip && \
    apt-get remove curl unzip && \
    rm -rf /var/lib/apt/lists/*
RUN ["cross-build-end"]
ENV PATH=$PATH:/usr/local/groovy${GROOVY_VERSION}/bin
WORKDIR /mnt
