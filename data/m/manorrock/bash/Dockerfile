FROM manorrock/debian
ENV BASH_VERSION=5.0-4
RUN apt-get update && \
    apt-get install -y bash=$BASH_VERSION && \
    rm -rf /var/lib/apt/lists/*
WORKDIR /mnt
