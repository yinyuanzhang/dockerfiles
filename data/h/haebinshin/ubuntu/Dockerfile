FROM ubuntu:14.04
MAINTAINER haebinshin <sunsal0704@gmail.com>

RUN sed -i 's/archive.ubuntu.com/kr.archive.ubuntu.com/' /etc/apt/sources.list

RUN apt-get update \
    && apt-get install -y curl locales \
    && rm -rf /var/lib/apt/lists/*

RUN locale-gen en_US.UTF-8

ENV LC_ALL=en_US.UTF-8
ENV LANG=en_US.UTF-8
ENV LANGUAGE=en_US.UTF-8

CMD ["/bin/bash"]
