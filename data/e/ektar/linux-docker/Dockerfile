from ektar/linux-ldap:v1.1.7
MAINTAINER eric@ds-do.com

RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | \
    apt-key add -
    
RUN add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

RUN export DEBIAN_FRONTEND=noninteractive && \
	apt-get update && apt install -qy \
	docker-ce \
&& rm -rf /var/lib/apt/lists/*

COPY startup.sh /data

COPY VERSION /ver-linux-docker-term

ENTRYPOINT ["/data/startup.sh"]

EXPOSE 22
