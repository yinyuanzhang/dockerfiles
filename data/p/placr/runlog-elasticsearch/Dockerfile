FROM      python:2.7

# grab gosu for easy step-down from root
RUN gpg --keyserver ha.pool.sks-keyservers.net --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4
RUN arch="$(dpkg --print-architecture)" \
	&& set -x \
	&& curl -o /usr/local/bin/gosu -fSL "https://github.com/tianon/gosu/releases/download/1.3/gosu-$arch" \
	&& curl -o /usr/local/bin/gosu.asc -fSL "https://github.com/tianon/gosu/releases/download/1.3/gosu-$arch.asc" \
	&& gpg --verify /usr/local/bin/gosu.asc \
	&& rm /usr/local/bin/gosu.asc \
	&& chmod +x /usr/local/bin/gosu

COPY      requirements.txt /tmp/
RUN       pip install -r /tmp/requirements.txt

# add our user and group first to make sure their IDs get assigned consistently, regardless of whatever dependencies get added
RUN       groupadd -r runlog && useradd -r -g runlog runlog

# Add the fill Elastic search from runlog script
RUN       mkdir -p /opt/runlog_to_elasticsearch
COPY 	  src/ /opt/runlog_to_elasticsearch/

COPY      docker-entrypoint.sh /

WORKDIR   /opt/runlog_to_elasticsearch

ENTRYPOINT ["/docker-entrypoint.sh"]

CMD       ["runlog"]
