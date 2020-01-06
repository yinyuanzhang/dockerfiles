FROM manorrock/raspbian:arm32v6
ENV RUBY_VERSION 1:2.5.1+b1
RUN ["cross-build-start"]
RUN apt-get update && \ 
    apt-get install -y ruby=$RUBY_VERSION && \
    rm -rf /var/lib/apt/lists/*
RUN ["cross-build-end"]
WORKDIR /mnt

