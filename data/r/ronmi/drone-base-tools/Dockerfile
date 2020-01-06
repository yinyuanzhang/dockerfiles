FROM debian:stable
MAINTAINER Ronmi Ren <ronmi.ren@gmail.com>

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
            ca-certificates wget curl ssh git \
 && apt-get clean \
 && rm -fr /var/lib/apt/lists/*

RUN echo '    StrictHostKeyChecking no' >> /etc/ssh/ssh_config
