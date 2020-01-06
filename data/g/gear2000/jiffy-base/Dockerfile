FROM gear2000/chef-solo
MAINTAINER Gary Leong <gwleong@gmail.com>

############################################################
#####Basic Pkgs - Public
############################################################
RUN echo "Installing Basic Pkgs" && \
    locale-gen en_US.UTF-8 && \
    dpkg-reconfigure locales && \
    export  LANG=en_US.UTF-8 && \
    export  LANGUAGE=en_US && \
    export  LC_ALL=en_US.UTF-8 && \
    apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10 && \
    apt-get update && \
    apt-get install -y pwgen wget curl git-core build-essential scons devscripts lintian dh-make \
    libpcre3 libpcre3-dev libboost-dev libboost-date-time-dev libboost-filesystem-dev \
    libboost-program-options-dev libboost-system-dev libboost-thread-dev \
    libpcap-dev libreadline-dev libssl-dev rng-tools haveged \
    openssh-server supervisor

RUN echo "Installing Docker Pkgs" && \
    apt-get -y install docker.io 

# Install docker-compose
RUN sh -c "curl -L https://github.com/docker/compose/releases/download/1.8.1/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose" && \
    chmod +x /usr/local/bin/docker-compose
RUN sh -c "curl -L https://raw.githubusercontent.com/docker/compose/1.8.1/contrib/completion/bash/docker-compose > /etc/bash_completion.d/docker-compose" 

RUN mkdir -p /var/run/sshd /var/log/supervisor
############################################################
#####Additional Pkgs - Public
############################################################
RUN apt-get update && \
    apt-get install htop vim sysstat -y && \
    apt-get install git python-dev rng-tools haveged -y && \
    apt-get install python-argparse python-paramiko python-setuptools python-yaml python-gridfs python-pip python-psutil -y && \
    apt-get purge python-prettytable -y 

#RUN pip uninstall gnupg -y 
#Must install and uninstall pymongo several times
RUN pip uninstall pymongo -y 
RUN pip install pymongo==2.7.2
RUN pip uninstall pymongo -y
RUN pip install pymongo==2.7.2

EXPOSE 22
