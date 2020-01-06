FROM kevinsimper/openbr

RUN sudo apt-get update && \
    sudo apt-get -y install software-properties-common
RUN sudo add-apt-repository ppa:ubuntu-lxc/lxd-stable && \
    sudo apt-get update && \
    sudo apt-get -y install golang
RUN pwd