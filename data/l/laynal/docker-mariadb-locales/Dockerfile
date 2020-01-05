FROM mariadb:latest

ENV LANG en_US.utf8

RUN apt-get update -y && \
	apt-get install -y locales locales-all && \
	rm -rf /var/lib/apt/lists/* && \
	localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8
