FROM manorrock/debian
ENV GIT_VERSION=1:2.20.1-2
RUN apt-get update && \
    apt-get install -y git=$GIT_VERSION && \
    rm -rf /var/lib/apt/lists/* 
WORKDIR /mnt

