FROM manorrock/debian
ENV CURL_VERSION=7.64.0-4
RUN apt-get update && \ 
    apt-get install -y curl=$CURL_VERSION && \
    rm -rf /var/lib/apt/lists/*
WORKDIR /mnt

