FROM centos:7

RUN yum-config-manager --add-repo  https://download.docker.com/linux/centos/docker-ce.repo && \ 
		yum install -y \
		git \
		java-1.8.0-openjdk  \
		java-1.8.0-openjdk-devel \
		rpm-build \
		ruby \
		ruby-devel \
		curl \
		zlib \
		gcc \
		libxml2-devel \
		zlib-devel \
		libxslt-devel \
		make \
                docker-ce && \
		yum clean all


COPY jenkins-docker-entrypoint.sh /usr/local/bin/

ENTRYPOINT []
