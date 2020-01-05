FROM centos:centos7
MAINTAINER Emmanuel CARRE <emmanuel.b.carre@gmail.com>

RUN	yum update -y && \
	yum install -y ruby \
		rubygem \
		rubygem-json \
		rubygem-parseconfig \
		git \
		ssh \
		zip \
		unzip \
		wget \
		make \
		gcc \
		openssl-devel && \
	wget -P /tmp http://downloads.sourceforge.net/proxytunnel/proxytunnel-1.9.0.tgz && \
	tar zxvf /tmp/proxytunnel-1.9.0.tgz -C /tmp/ && \
	make -C /tmp/proxytunnel-1.9.0/ && \
	make -C /tmp/proxytunnel-1.9.0/ install && \
	rm -rf /tmp/proxytunnel-1.9.0 /tmp/proxytunnel-1.9.0.tgz && \
	gem install rhc && \
	gem update rhc

CMD ["bash"]
