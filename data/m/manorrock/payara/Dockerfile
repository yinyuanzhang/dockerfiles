FROM manorrock/zulu:arm32v6
ENV PAYARA_VERSION=5.193.1
RUN ["cross-build-start"]
RUN apt-get update && \
    apt-get install -y curl unzip && \
    cd /usr/local && \
    curl -O https://repo.maven.apache.org/maven2/fish/payara/distributions/payara/$PAYARA_VERSION/payara-$PAYARA_VERSION.zip && \
    unzip payara-$PAYARA_VERSION.zip && \
    rm payara-$PAYARA_VERSION.zip && \
    rm -rf /var/lib/apt/lists/*
CMD ["/usr/local/payara5/bin/asadmin", "start-domain", "-v"]
EXPOSE 8080
WORKDIR /mnt
RUN ["cross-build-end"]
