FROM ubuntu:14.04
MAINTAINER Eric Schultz <eric@startuperic.com>

ENV DEBIAN_FRONTEND noninteractive

RUN locale-gen en_US en_US.UTF-8

RUN apt-get update -q
RUN apt-get install -qy --force-yes git-core python
RUN git clone https://github.com/RuudBurger/CouchPotatoServer.git /opt/couchpotato

VOLUME /config
VOLUME /data

EXPOSE 5050

ENTRYPOINT ["python", "/opt/couchpotato/CouchPotato.py"]
CMD ["--data_dir=/config"]