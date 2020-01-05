FROM centos:latest

# A base fmi image with proper repositories in place

# These repos are unnecessary ...
# They cause update problems in certain versions
RUN rm -f /etc/yum.repos.d/CentOS-Vault.repo /etc/yum.repos.d/CentOS-Sources.repo

# Prepare CI build scripts
COPY ci-build.sh /usr/local/bin/ci-build.sh
RUN ln -s ci-build.sh /usr/local/bin/ci-build

# FMI proxy setup if needed
COPY proxydetect.sh /usr/local/bin/proxydetect.sh
RUN ln -s proxydetect.sh /usr/local/bin/proxydetect

# Wrapper for uid manipulation and other stuff
COPY wrapper.sh /usr/local/bin/wrapper.sh

# Lock some library versions to prevent updates breaking smartmet-server
COPY versionlock.list /etc/yum/pluginconf.d/versionlock.list

# Basic setup before running any yum commands
RUN echo ip_resolve=4 >> /etc/yum.conf && \
    . /usr/local/bin/proxydetect && \
    curl -O /etc/yum.repos.d/libjpeg-turbo.repo https://libjpeg-turbo.org/pmwiki/uploads/Downloads/libjpeg-turbo.repo

# Install gosu
ENV GOSU_VERSION 1.10
RUN set -ex; . /usr/local/bin/proxydetect; \
	\
	yum -y install epel-release; \
	yum -y install wget; \	
	yum -y install dpkg; \
	\
	dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')"; \
	wget --quiet -O /usr/bin/gosu "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch"; \
	wget --quiet -O /tmp/gosu.asc "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch.asc"; \
# verify the signature
	export GNUPGHOME="$(mktemp -d)"; \
#	gpg --keyserver ha.pool.sks-keyservers.net --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4 ; \
#	gpg --batch --verify /tmp/gosu.asc /usr/bin/gosu; \
	rm -fr "$GNUPGHOME" /tmp/gosu.asc; \
	chmod +xs /usr/bin/gosu; \
# verify that the binary works
	gosu nobody true; \
	yum -y remove dpkg ; \
	yum clean all && \
 	rm -rf /tmp/* /var/cache/yum

# Preinstall some packeges and enable extra repositories
# Yum has a (mis)feature where the return value is 0 for multiple packages if any of them succeed.
# Have to run every install in a single command as they all need to succeed.
# Other extra things:
#  - install libpqxx from Postgresql 9.5 repos but disable thet repo after it
#  - reinstall glibc-common with changed lang settings. Otherwise we get errors when using locales.
RUN . /usr/local/bin/proxydetect && \
 yum -y install deltarpm && \
 yum -y install rpm-build && \
 yum -y install yum-plugin-versionlock && \
 yum -y install https://download.fmi.fi/smartmet-open/rhel/7/x86_64/smartmet-open-release-17.9.28-1.el7.fmi.noarch.rpm && \
 yum -y install https://download.fmi.fi/fmiforge/rhel/7/x86_64/fmiforge-release-17.9.28-1.el7.fmi.noarch.rpm && \
 yum -y install ccache && \
 yum -y install createrepo_c && \
 yum -y install git && \
 yum -y install make && \
 yum -y install sudo && \
 yum -y install rpmlint && \
 yum -y install yum-utils && \
 yum -y install https://download.postgresql.org/pub/repos/yum/9.5/redhat/rhel-7-x86_64/pgdg-redhat95-9.5-3.noarch.rpm && \
 yum -y install libpqxx && \
 yum -y install libpqxx-devel && \
 rpm -e pgdg-redhat95 && \
 yum -y update && \
 yum -y reinstall --setopt=override_install_langs='' --setopt=tsflags='' glibc-common && \
 yum clean all && \
 rm -rf /var/cache/yum

## Configure sudo
RUN mkdir -p /etc/sudoers.d && echo 'ALL ALL=(ALL) NOPASSWD: ALL' > /etc/sudoers.d/all && \
	useradd rpmbuild

## Install CirleCI CLI
RUN curl -fLSs https://circle.ci/cli | bash

# Cleanup, leave YUM cache empty initially 
RUN \
 yum clean all && \
 rm -rf /var/cache/yum && \
 mkdir -p /var/cache/yum && \
 rm -f /root/anaconda-ks.cfg /anaconda-post.log && \
 mkdir -p /dist && \
 chmod 4777 /dist/. && \
 rm -rf /tmp/*

# Prepare ccache usage. Build timeouts are greatly reduced, if
# /ccache is mounted from host environment
RUN mkdir -m 777 /ccache && \
    echo cache_dir=/ccache > /etc/ccache.conf && \
    echo umask=000 >> /etc/ccache.conf && \
    ln -s /usr/bin/ccache /usr/local/bin/c++ && \
    ln -s /usr/bin/ccache /usr/local/bin/g++ && \
    ln -s /usr/bin/ccache /usr/local/bin/gcc && \
    ln -s /usr/bin/ccache /usr/local/bin/cc

# Keep yum cache around
# Useful for multiple runs of the same machine, if /var/cache/yum is mounted from host environment.
# This step must be done in the end so that yum is not going to be
# used anymore on docker build. Otherwise intermediate containers
# may become large accidentally.
# Also make some other last minute modifications
RUN sed -i -e 's/keepcache=0//' /etc/yum.conf && \
    echo keepcache=1 >> /etc/yum.conf && \
    echo 'PATH=/usr/local/bin:$PATH' >> /etc/bashrc && \
    echo 'export PATH' >> /etc/bashrc

# Run final stuff as rpmbuild
USER rpmbuild

# Always run certain autodetection steps
# Sadly, CircleCI Local CLI apparently overrides entrypoint
ENTRYPOINT [ "/usr/local/bin/wrapper.sh" ]

# Run shell
CMD ["/bin/bash"]

VOLUME /var/cache/yum
VOLUME /ccache
