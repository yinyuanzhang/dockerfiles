FROM phusion/baseimage:0.10.1
LABEL maintainer="Graham Stewart <graham.stewart@findyourcanopy.com>"

USER	root
RUN	apt-get update && apt-get upgrade -y -o Dpkg::Options::="--force-confold" && \
	curl -sL https://deb.nodesource.com/setup_10.x | bash - && \
	apt-get install -y nodejs phantomjs telnet --no-install-recommends && \
	rm -f /etc/service/sshd/down && \
	/etc/my_init.d/00_regen_ssh_host_keys.sh && \
        apt-get autoremove -y && \
        apt-get clean && \
	rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

CMD ["/sbin/my_init"]

