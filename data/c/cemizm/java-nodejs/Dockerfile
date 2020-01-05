FROM java:8
MAINTAINER Cem Basoglu "cem.basoglu@web.de"

RUN apt-get -y update ; apt-get -y install curl && \
	curl -sL https://deb.nodesource.com/setup_7.x | bash  && \
	apt-get -y install nodejs && \
	npm -g install bower

RUN echo '{ "allow_root": true }' > /root/.bowerrc