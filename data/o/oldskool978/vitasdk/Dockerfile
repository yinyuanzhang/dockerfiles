FROM ubuntu:18.04
MAINTAINER David Cache <recordingexperts@gmail.com>


USER root
WORKDIR /build

RUN \
    apt-get --assume-yes update && \
    apt-get --assume-yes install sudo && \
    useradd -ms /bin/bash developer && \
    echo "developer" | adduser developer sudo && \
    passwd -d developer && \
    echo "developer  ALL=(ALL:ALL) ALL" >> /etc/sudoers 


USER developer
WORKDIR /home/developer

RUN \
    mkdir Downloads && \
    cd Downloads && \
    sudo apt-get --assume-yes update && sudo apt-get --assume-yes upgrade && \
    sudo apt-get --assume-yes install apt-utils dialog software-properties-common dos2unix nano vim git && \
    git clone https://github.com/oldskool978/vitasdk-linux-installer.git && \
    cd ./vitasdk-linux-installer

ENV VITASDK /usr/local/vitasdk
ENV PATH $PATH:$VITASDK/bin

USER root      
RUN \ 
     cd /home/developer/Downloads/vitasdk-linux-installer && \
     su developer -c 'export PATH=$(pwd)/../vita-makepkg:$VITASDK/bin:$PATH && bash vitasdk.sh && \
     rm -rf /home/developer/Downloads' 
     
USER developer
WORKDIR /home/developer


CMD ["/bin/bash"]
