FROM thousandeyes/enterprise-agent

ADD .updated /

RUN apt-get update && \
	apt-get -y dist-upgrade && \
	apt-get clean all
