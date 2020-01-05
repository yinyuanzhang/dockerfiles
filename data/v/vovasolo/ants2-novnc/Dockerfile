# This Dockerfile creates standalone ANTS2 installation accessible through
# an HTML5 browser or a vnc viewer 
# Based on headless vnc/novnc container by Tobias Schneck "tobias.schneck@consol.de"

FROM ubuntu:18.04

## Connection ports for controlling the UI:
# VNC port:5901
# noVNC webport, connect via http://IP:6901/?password=vncpassword
ENV DISPLAY=:1 \
    VNC_PORT=5901 \
    NO_VNC_PORT=6901
EXPOSE $VNC_PORT $NO_VNC_PORT

### Envrionment config
ENV HOME=/headless \
    TERM=xterm \
    STARTUPDIR=/dockerstartup \
    INST_SCRIPTS=/headless/install \
    NO_VNC_HOME=/headless/noVNC \
    DEBIAN_FRONTEND=noninteractive \
    VNC_COL_DEPTH=24 \
    VNC_RESOLUTION=1280x1024 \
    VNC_PW=vncpassword \
    VNC_VIEW_ONLY=false
WORKDIR $HOME

### Add all install scripts for further steps
ADD ./src/common/install/ $INST_SCRIPTS/
ADD ./src/ubuntu/install/ $INST_SCRIPTS/
RUN find $INST_SCRIPTS -name '*.sh' -exec chmod a+x {} +

### Install some common tools
RUN $INST_SCRIPTS/tools.sh
ENV LANG='en_US.UTF-8' LANGUAGE='en_US:en' LC_ALL='en_US.UTF-8'

### Install xvnc-server & noVNC - HTML5 based VNC viewer
RUN $INST_SCRIPTS/tigervnc.sh
RUN $INST_SCRIPTS/no_vnc.sh

### Install firefox and chrome browser
# RUN $INST_SCRIPTS/firefox.sh
# RUN $INST_SCRIPTS/chrome.sh

### Install xfce UI
RUN $INST_SCRIPTS/xfce_ui.sh
ADD ./src/common/xfce/ $HOME/

### configure startup
RUN $INST_SCRIPTS/libnss_wrapper.sh
ADD ./src/common/scripts $STARTUPDIR
RUN $INST_SCRIPTS/set_user_permission.sh $STARTUPDIR $HOME

# ANTS stuff

ARG ROOTTGZ=root_v6.14.04.Linux-ubuntu18-x86_64-gcc7.3.tar.gz
# Update all packages
RUN apt-get -y update && apt-get -y upgrade && apt-get -y dist-upgrade
# Install packages
# Essential utilities
RUN apt-get -y install git nano wget
# Development environment (gcc, make, etc. + cmake)
RUN apt-get -y install build-essential cmake
# Qt5 base system + modules required by ANTS
RUN apt-get -y install qt5-default libqt5websockets5-dev qtscript5-dev
# additional libs needed by ROOT
RUN apt-get -y install libtbb-dev
# additional libs needed by ANTS
RUN apt-get -y install libeigen3-dev
# xeyes to test X11 forwarding + some X11 packaged needed by ROOT pulled as dependencies
RUN apt-get -y install x11-apps
# OpenGL, FLANN and FANN
RUN apt-get -y install libgl2ps-dev libflann-dev libfann-dev liblz4-dev
# Python scripting
RUN apt-get -y install python3-dev libpythonqt-qt5-python3-dev

# ROOT Installation
RUN wget https://root.cern.ch/download/$ROOTTGZ
RUN tar -xzf $ROOTTGZ -C /opt
RUN rm $ROOTTGZ
RUN echo ". /opt/root/bin/thisroot.sh" >> ~/.bashrc

# Ncrystal
RUN cd / && git clone https://github.com/mctools/ncrystal.git # refresh+1!
RUN cd /ncrystal && cmake . && make -j3 && make install
RUN echo "export LD_LIBRARY_PATH=\$LD_LIBRARY_PATH:/usr/local/lib" >> ~/.bashrc
#ENV LD_LIBRARY_PATH="/usr/local/lib:${LD_LIBRARY_PATH}"


# ANTS installation
RUN mkdir /ants2 && cd /ants2 && git clone -b Dev https://github.com/andrmor/ANTS2.git # refresh+1!
RUN cd /ants2/ANTS2 && mkdir build

### the effect of sourcing a script lasts only inside one RUN command
### so we need to pack it together with compilation as a one-liner
RUN /bin/bash -c "source /opt/root/bin/thisroot.sh \
    && cd /ants2/ANTS2/build && qmake \"CONFIG += ants2_docker\" ../src/ants2.pro && make -j3"
RUN mkdir /root/.config && mkdir /root/.config/ants2 && mkdir /root/.config/ants2/Config
RUN touch /root/.config/ants2/Config/config.ini

# End of ANTS stuff

RUN useradd -ms /bin/bash formiga

USER 1000

ENTRYPOINT ["/dockerstartup/vnc_startup.sh"]
CMD ["--wait"]
