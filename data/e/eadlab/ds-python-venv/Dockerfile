FROM centos:latest
MAINTAINER Dinesh <hyperties@gmail.com>

# === COPY FILES ===

COPY requirements.txt /root/requirements.txt
COPY alias.sh /root/alias.sh
COPY pip.conf /root/pip.conf

# === SET ENVIRONMENT VARIABLES ===

#ENV PATH=""
#ENV LANGUAGE en_US.UTF-8
#ENV LANG en_US.UTF-8

# === INSTALL DEPENDENCIES ===

WORKDIR /root

RUN yum -y install bzip2 \
                   curl \
                   curl-devel \
                   perl-devel \
                   perl-CPAN \
                   tmux \
                   wget \
                   which \
                   zlib-devel \
	&& yum -y groupinstall "Development Tools" \
	&& yum -y remove git \
	&& yum -y install https://centos7.iuscommunity.org/ius-release.rpm \
	&& yum -y install git2u-core.x86_64 \
					  python36u \
					  python36u-pip \
					  python36u-devel \
	&& wget https://download.opensuse.org/repositories/shells:fish:release:2/CentOS_7/shells:fish:release:2.repo -P /etc/yum.repos.d/ \
	&& yum install -y fish \					  
	&& yum -y autoremove \
	&& yum clean all \
	&& rm -rf /var/cache/yum \
	&& cat alias.sh >> ~/.bashrc \
	&& source ~/.bash_profile

WORKDIR /home

RUN python3.6 -m venv ds-py3 \
	&& source ds-py3/bin/activate \
	&& pip install virtualenv \
	&& pip install -r /root/requirements.txt \
	&& rm -rf ~/.cache/pip


# === INITIALIZE ===

COPY start.sh /etc/profile.d/

WORKDIR /home
EXPOSE 8080
CMD /usr/bin/bash