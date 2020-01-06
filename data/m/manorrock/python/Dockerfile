FROM manorrock/raspbian:arm32v6
RUN ["cross-build-start"]
ENV PYTHON_VERSION=3.7.3-1
RUN apt-get update && \
    apt-get install -y python3=$PYTHON_VERSION && \
    rm -rf /var/lib/apt/lists/*
WORKDIR /mnt
RUN ["cross-build-end"]
