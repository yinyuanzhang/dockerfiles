# Pull base image.
FROM ubuntu:18.04

############################################################
# Basic Pkgs - Public
############################################################
# apt-get install -y locales-all && \
#    locale-gen en_US.UTF-8 && \
#    dpkg-reconfigure locales && \

RUN apt-get clean && apt-get update && \
    apt-get install -y --no-install-recommends gnupg || rm -rf /var/lib/apt/lists/*

RUN echo "Installing Basic Pkgs" && \
    export  LANG=en_US.UTF-8 && \
    export  LANGUAGE=en_US && \
    export  LC_ALL=en_US.UTF-8 && \
    apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10 && \
    apt-get clean && apt-get update && \
    apt-get install -y --no-install-recommends \
    pwgen wget curl git-core build-essential scons devscripts lintian dh-make \
    libpcre3 libpcre3-dev libboost-dev libboost-date-time-dev libboost-filesystem-dev \
    libboost-program-options-dev libboost-system-dev libboost-thread-dev \
    libpcap-dev libreadline-dev libssl-dev rng-tools haveged rsync\
    openssh-server supervisor unzip vim software-properties-common || rm -rf /var/lib/apt/lists/*

############################################################
# Install Docker packages
############################################################
RUN echo "Installing Docker Pkgs" && \
    apt-get clean && apt-get update && \
    apt-get -y --no-install-recommends install docker.io || rm -rf /var/lib/apt/lists/*

# Install docker-compose
RUN sh -c "curl -L https://github.com/docker/compose/releases/download/1.8.1/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose" && \
    chmod +x /usr/local/bin/docker-compose
RUN sh -c "curl -L https://raw.githubusercontent.com/docker/compose/1.8.1/contrib/completion/bash/docker-compose > /etc/bash_completion.d/docker-compose"

RUN mkdir -p /var/run/sshd /var/log/supervisor

############################################################
# Additional Pkgs - Public
############################################################
RUN apt-get clean && apt-get update && \
    apt-get install htop sysstat -y --no-install-recommends && \
    apt-get install git python-dev rng-tools haveged -y --no-install-recommends && \
    apt-get install python-argparse python-paramiko python-setuptools python-yaml python-gridfs python-pip python-psutil -y --no-install-recommends && \
    apt-get purge python-prettytable -y || rm -rf /var/lib/apt/lists/*

################################
# Install Terraform
################################
RUN cd /tmp && wget https://releases.hashicorp.com/terraform/0.12.12/terraform_0.12.12_linux_amd64.zip && \
    unzip terraform_0.12.12_linux_amd64.zip && \
    mv terraform /usr/local/bin/

# Check that it's installed
RUN terraform --version

################################
# Install Ansible
################################
RUN apt-add-repository --yes --update ppa:ansible/ansible
RUN apt-get clean && apt-get update && \
    apt-get install ansible -y --no-install-recommends || rm -rf /var/lib/apt/lists/*

################################
# Install Jiffy Dependency Python
################################
ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

################################
# Clean up Image
################################
RUN apt-get clean && rm -rf /tmp/* && rm -rf /var/lib/apt/lists/*

#EXPOSE 22

#################################
## Install python
#################################
#
#RUN apt-get install -y python3-pip
##RUN ln -s /usr/bin/python3 python
#RUN pip3 install --upgrade pip
#RUN python3 -V
#RUN pip --version
#
#################################
## Install AWS CLI
#################################
#RUN pip install awscli --upgrade --user
#
## add aws cli location to path
#ENV PATH=~/.local/bin:$PATH
#
## Adds local templates directory and contents in /usr/local/terrafrom-templates
#ADD templates /usr/local/bin/templates
#
#RUN mkdir ~/.aws && touch ~/.aws/credentials
