FROM ubuntu:latest

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && \
    apt-get -y install build-essential valgrind cppcheck dnsutils

RUN apt-get clean && rm -rf /var/lib/apt/lists/*

CMD ["/bin/bash"]
