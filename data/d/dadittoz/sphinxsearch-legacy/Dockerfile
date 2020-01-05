FROM debian:jessie
MAINTAINER daditto <daditto@gmail.com>
ENV DEBIAN_FRONTEND noninteractive
ADD /etc/apt /etc/apt
RUN apt-get update && \
	apt-get upgrade -y && \
	apt-get install -y ca-certificates inotify-tools unrar unzip curl wget supervisor libmysqlclient18 && \
	apt-get clean && \
	echo -n > /var/lib/apt/extended_states
RUN useradd -u 500 core
RUN wget -q http://sphinxsearch.com/files/sphinxsearch_2.2.10-release-1~jessie_amd64.deb -O /tmp/sphinx.deb
RUN dpkg -i /tmp/sphinx.deb || apt-get -y -f install
RUN rm /tmp/sphinx.deb
RUN mkdir /config /data /data/index
ADD config /config

ADD etc /etc

VOLUME /data

RUN chmod +x /config/loop
CMD /config/loop

EXPOSE 9001 9306 9312
