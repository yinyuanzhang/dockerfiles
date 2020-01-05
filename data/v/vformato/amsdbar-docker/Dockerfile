FROM cern/slc6-base

MAINTAINER Valerio Formato valerio.formato@cern.ch

#--- Environment variables
ENV AMS_USER="amsuser"
ENV AMS_USER_HOME="/home/amsuser"

#--- Patch yum for docker
RUN yum install -y yum-plugin-ovl

#--- make sure FUSE can be enabled
RUN if [[ ! -e /dev/fuse ]]; then mknod -m 666 /dev/fuse c 10 229; fi

#--- install cvmfs repos
ADD etc-yum-cernvm.repo /etc/yum.repos.d/cernvm.repo

#--- Install rpms
RUN yum update -y; yum clean all
RUN yum -y install \
    cvmfs cvmfs-init-scripts cvmfs-auto-setup \
    freetype fuse sudo glibc-devel glibc-headers libstdc++-devel \
    man nano emacs openssh-server openssl098e libXext libXpm \
    git gsl-devel freetype-devel libSM libX11-devel libXext-devel make gcc-c++ \
    gcc binutils libXpm-devel libXft-devel boost-devel \
    cmake ncurses ncurses-devel xrootd blas; \
    yum clean all
RUN yum install -y cvs openssh-clients

WORKDIR /root


#--- add files last (as this invalids caches)
ADD etc-cvmfs-default-local /etc/cvmfs/default.local
ADD etc-cvmfs-config-local  /etc/cvmfs/config.d/ams.cern.ch.local

ADD run-cvmfs.sh /root/run-cvmfs.sh
RUN chmod u+x /root/run-cvmfs.sh

RUN mkdir -p \
    /cvmfs/ams.cern.ch \
    /cvmfs/sft.cern.ch

RUN echo "ams.cern.ch         /cvmfs/ams.cern.ch cvmfs defaults 0 0" >> /etc/fstab && \
    echo "sft.cern.ch         /cvmfs/sft.cern.ch cvmfs defaults 0 0" >> /etc/fstab

# Setting up a user
RUN adduser $AMS_USER -d $AMS_USER_HOME && echo "$AMS_USER:ams" | chpasswd && \
    echo "$AMS_USER ALL=(root) NOPASSWD:ALL" > /etc/sudoers.d/$AMS_USER && \
    chmod 0440 /etc/sudoers.d/$AMS_USER
RUN chown -R $AMS_USER $AMS_USER_HOME

# ADD setup_amsenv.sh  $AMS_USER_HOME
# RUN chown -R $AMS_USER $AMS_USER_HOME/setup_amsenv.sh

ADD dot-bashrc  $AMS_USER_HOME/.bashrc
RUN chown $AMS_USER $AMS_USER_HOME/.bashrc
# RUN chmod u+x $AMS_USER_HOME/setup_amsenv.sh

USER $AMS_USER
WORKDIR $AMS_USER_HOME
