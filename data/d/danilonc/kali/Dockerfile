FROM kalilinux/kali-linux-docker:latest
MAINTAINER danilonc

RUN apt-get update -y &&\
    apt-get dist-upgrade -y &&\
    apt-get autoremove -y &&\
    apt-get install -y apt-file build-essential cmake command-not-found curl git ipython masscan metasploit-framework nmap ncat python3-colorama python3-dev python3-pip python3-prompt-toolkit python3-pygments python3-setuptools python3-termcolor python3-terminaltables python-ipython python-pip spike time tmux vim zmap zsh hcxtools magic-wormhole

RUN apt-file update && update-command-not-found

# Download capstone, keystone and unicorn source-code
WORKDIR /opt
RUN git clone https://github.com/keystone-engine/keystone.git
RUN git clone https://github.com/aquynh/capstone.git
RUN git clone https://github.com/unicorn-engine/unicorn.git

# Build Capstone
WORKDIR /opt/capstone
RUN git checkout tags/3.0.5
RUN ./make.sh && ./make.sh install

# Build Keystone
WORKDIR /opt/keystone
RUN git checkout tags/0.9.1
RUN mkdir build
WORKDIR /opt/keystone/build
RUN ../make-lib.sh && make install
RUN ../make-share.sh && make install

# Build unicorn
WORKDIR /opt/unicorn
RUN git checkout tags/1.0.1
RUN mkdir build
RUN ./make.sh && ./make.sh install 

# ldconfig new libraries
RUN ldconfig

# Install python keybinds
RUN pip install --upgrade keystone-engine capstone unicorn

# Install pwntools
RUN pip install pwntools

WORKDIR /opt

# Install shellen 
RUN pip3 install shellen

# Install kcshell
RUN pip3 install kcshell

# Install radare2
RUN git clone https://github.com/radare/radare2.git
RUN ./radare2/sys/install.sh

# Default home dir
WORKDIR /root
