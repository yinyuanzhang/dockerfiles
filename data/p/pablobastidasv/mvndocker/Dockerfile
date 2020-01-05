FROM maven:3-jdk-11-slim

RUN apt-get update && \
    apt-get install -y git && \
    apt-get clean autoclean  && \
    apt-get autoremove --yes && \
    rm -rf /var/lib/{apt,dpkg,cache,log}

RUN curl https://download.docker.com/linux/debian/dists/stretch/pool/stable/amd64/docker-ce-cli_18.09.6~3-0~debian-stretch_amd64.deb --output docker.deb && \
    dpkg -i docker.deb && \
    rm -rf docker.deb && \
    rm -rf /var/lib/{apt,dpkg,cache,log}
