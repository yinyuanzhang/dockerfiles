FROM debian:stretch-slim

RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg2 \
    sudo \
    software-properties-common \
    wget 


# Update & upgrade packages
RUN apt-get -y upgrade && \
        apt-get clean autoclean && \
        apt-get autoremove -y

# install locales languages to set US text
RUN apt-get update && \
        DEBIAN_FRONTEND=noninteractive \
        apt-get install -y locales

# set language to US
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    dpkg-reconfigure --frontend=noninteractive locales && \
    update-locale LANG=en_US.UTF-8
ENV LANG en_US.UTF-8 

# adding a base developer acc for specific apps
RUN export uid=1000 gid=1000 && \
    mkdir -p /home/developer && \
    echo "developer:x:${uid}:${gid}:Developer,,,:/home/developer:/bin/bash" >> /etc/passwd && \
    echo "developer:x:${uid}:" >> /etc/group && \
    echo "developer ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/developer && \
    chmod 0440 /etc/sudoers.d/developer && \
    chown ${uid}:${gid} -R /home/developer