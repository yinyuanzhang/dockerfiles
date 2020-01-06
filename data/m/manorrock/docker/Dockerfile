FROM manorrock/raspbian:arm32v6 
RUN ["cross-build-start"]
RUN apt-get update && \
    apt-get install -y curl && \
    rm -rf /var/lib/apt/lists/* && \
    curl -sSL https://get.docker.com | bash
WORKDIR /mnt
RUN ["cross-build-end"]

