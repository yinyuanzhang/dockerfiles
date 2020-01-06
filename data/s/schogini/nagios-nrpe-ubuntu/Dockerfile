
FROM ubuntu:trusty

MAINTAINER Sreeprakash Neelakantan <sree@schogini.com>

RUN apt-get update && \
    apt-get install -y nano wget tree && \
    apt-get install -y nagios-nrpe-server nagios-plugins

COPY Dockerfile /

# docker build -t schogini/nagios-nrpe-ubuntu .
# run -ti --rm --name nrpe1 --hostname nrpe1 -P schogini/nagios-nrpe-ubuntu
#root@nrpe1:/# nano /etc/nagios/nrpe.cfg
#root@nrpe1:/# /etc/init.d/nagios-nrpe-server restart

