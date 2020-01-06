# Use latest ubuntu image as the base
FROM ubuntu:18.04
# Update all packages
RUN apt-get -y update && apt-get -y upgrade && apt-get -y dist-upgrade
# Install packages
# Essential utilities
RUN apt-get -y install git nano wget
# Development environment (gcc, make, etc.)
RUN apt-get -y install build-essential
# Qt5 base system + modules required by ANTS
RUN apt-get -y install qt5-default libqt5websockets5-dev qtscript5-dev
# additional libs needed by ROOT
RUN apt-get -y install libtbb-dev
# additional libs needed by ANTS
RUN apt-get -y install libeigen3-dev
# xeyes to test X11 forwarding + some X11 packaged needed by ROOT pulled as dependencies
RUN apt-get -y install x11-apps

# ROOT Installation
RUN wget https://root.cern.ch/download/root_v6.14.00.Linux-ubuntu18-x86_64-gcc7.3.tar.gz
RUN tar -xzf root_v6.14.00.Linux-ubuntu18-x86_64-gcc7.3.tar.gz -C /opt
RUN rm root_v6.14.00.Linux-ubuntu18-x86_64-gcc7.3.tar.gz
RUN echo ". /opt/root/bin/thisroot.sh" >> ~/.bashrc

# ANTS installation
RUN mkdir /ants2 && cd ants2 && git clone -b Dev https://github.com/andrmor/ANTS2.git # refresh+1!
RUN cd /ants2/ANTS2 && mkdir build
### the effect of sourcing a script lasts only inside one RUN command
### so we need to pack it together with compilation as a one-liner
RUN /bin/bash -c "source /opt/root/bin/thisroot.sh \
    && cd /ants2/ANTS2/build && qmake \"CONFIG += Headless\" ../src/ants2.pro && make -j3"
RUN mkdir /root/.config && mkdir /root/.config/ants2 && mkdir /root/.config/ants2/Config
RUN touch /root/.config/ants2/Config/config.ini

# Install Dispatcher
RUN cd /ants2 && git clone https://github.com/andrmor/ServDisp.git && cd ServDisp && mkdir build
RUN cd /ants2/ServDisp/build && qmake ../ServDisp.pro && make -j3
COPY config.json /ants2/ServDisp/build/

#RUN gcc -march=native -E -v - </dev/null 2>&1 | grep cc1

CMD ["/bin/bash"]

