FROM acuve/docker-encoding-farm

MAINTAINER ACUVE sub_chon@yahoo.co.jp

# Set Locale

RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8
ENV USER root


# Enable Universe and Multiverse and install dependencies.

RUN echo deb http://archive.ubuntu.com/ubuntu precise universe multiverse >> /etc/apt/sources.list; apt-get update; apt-get -y install autoconf automake build-essential git mercurial cmake libtool pkg-config texi2html wget yasm vim zsh xfce4 xfce4-goodies tightvncserver language-pack-ja fonts-vlgothic firefox ruby mikutter emacs clang libboost-all-dev libqt4-dev xfce4-terminal; apt-get clean

# Install dotfiles
RUN cd /root; git clone --recursive --depth 1  https://github.com/ACUVE/dotfiles; cd /root/dotfiles; ./install.sh

# Change Default Shell
RUN chsh -s /bin/zsh

CMD ["/bin/zsh"]
