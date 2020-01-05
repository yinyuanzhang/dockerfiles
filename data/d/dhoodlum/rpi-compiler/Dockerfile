FROM debian
RUN apt update
RUN apt full-upgrade -y
RUN apt install -y build-essential libncurses5-dev
RUN apt install -y automake libtool bison flex texinfo
RUN apt install -y gawk curl cvs subversion gcj-jdk
RUN apt install -y libexpat1-dev python-dev
RUN apt install -y git
RUN cd $HOME && git clone --branch 1.22 https://github.com/crosstool-ng/crosstool-ng.git
RUN cd $HOME/crosstool-ng && autoconf
RUN apt install -y gperf
RUN apt install -y wget
RUN apt install -y help2man
RUN apt install -y libtool-bin
RUN cd $HOME/crosstool-ng && ./configure
RUN cd $HOME/crosstool-ng && make
RUN cd $HOME/crosstool-ng && make install

# create developer user
RUN useradd -ms /bin/bash developer
USER developer
RUN mkdir $HOME/armv7l
RUN cd $HOME/armv7l && ct-ng armv7-rpi2-linux-gnueabihf
RUN cd $HOME/armv7l && ct-ng build
ENV PATH $PATH:/home/developer/x-tools/armv7-rpi2-linux-gnueabihf/bin
RUN mkdir /home/developer/src

# install ib
RUN cd $HOME && git clone https://github.com/JasonL9000/ib.git
ENV PATH $PATH:/home/developer/ib
