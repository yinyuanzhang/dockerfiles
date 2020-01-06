FROM ubuntu:18.04

RUN ln -fs /usr/share/zoneinfo/Europe/London /etc/localtime
RUN sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list && \
    apt update && \
    apt -y upgrade && \
    apt install -y build-essential && \
    apt install -y software-properties-common && \
    apt install -y byobu curl git git-lfs htop man unzip vim wget
RUN mkdir /root/Downloads && mkdir /root/Desktop
RUN git clone https://github.com/PSOPT/psopt /root/psopt/
RUN cd /root/psopt/ && \
    sed 's/sudo //g' install-ubuntu-18.04.sh > sudoless-install-ubuntu-18.04.sh && \
    sh ./sudoless-install-ubuntu-18.04.sh

VOLUME ["/root/psopt/"]

CMD ["/bin/bash"]
