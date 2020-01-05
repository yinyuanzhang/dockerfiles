#Dockerfile for MOIL-Ubuntu

FROM ubuntu:latest
MAINTAINER anto "m07158031@o365.mcut.edu.tw"

USER root
WORKDIR /root

RUN apt-get update 
RUN apt-get install -y nano git make sudo tree curl wget 

RUN apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip


# Create user "docker" with sudo powers
RUN useradd -m docker && \
    usermod -aG sudo docker && \
    echo '%sudo ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers && \
    cp /root/.bashrc /home/docker/ && \
    mkdir /home/docker/data && \
    chown -R --from=root docker /home/docker

# Use C.UTF-8 locale to avoid issues with ASCII encoding
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

WORKDIR /home/docker/data
ENV HOME /home/docker
ENV USER docker
USER docker
ENV PATH /home/docker/.local/bin:$PATH

# Avoid first use of sudo warning.
RUN touch $HOME/.sudo_as_admin_successful

CMD [ "/bin/bash" ]
