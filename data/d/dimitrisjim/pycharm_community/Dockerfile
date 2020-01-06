####################
# PyCharm Community 
####################

FROM ubuntu:14.04
MAINTAINER Jim Fasarakis-Hilliard "d.f.hilliard@gmail.com"

# Set some ENV variables.
ENV IDE_PATH=/home/ \
 HOME=/home/dev/

# Add user dev so the container doesn't run as root.
RUN useradd dev \
 && echo "dev:developer" | chpasswd \
 && usermod -s /bin/bash dev \
 && usermod -aG sudo dev

# Install dependencies.
RUN apt-get -yqq update && apt-get -yqq install \
 wget \
 git \
 mercurial \
 subversion \
 openjdk-7-jdk 

WORKDIR $IDE_PATH
COPY py_setup.sh $IDE_PATH

# Install python 2.7.9 & 3.4.3
RUN ./py_setup.sh 

# Get pycharm tarball.
RUN wget http://download.jetbrains.com/python/pycharm-community-4.0.6.tar.gz \ 
 && tar -xf pycharm-community-4.0.6.tar.gz \
 && rm -rf *.tar.gz \
 && mv pycharm* pycharm

RUN apt-get clean 

VOLUME $IDE_PATH
WORKDIR $HOME

ENV PATH $IDE_PATH/pycharm/bin:$PATH
CMD ["pycharm.sh"]
