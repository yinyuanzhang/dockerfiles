FROM ubuntu:14.04

## Install tools
RUN apt-get update && \
    apt-get install software-properties-common supervisor -y 

## Install salt-stack
# add ppa repository
RUN add-apt-repository ppa:saltstack/salt && \
    apt-get update
# install salt master
RUN apt-get install salt-master -y

## Supervisor configuration
ADD config/supervisor-salt.conf /etc/supervisor/conf.d/salt.conf

## Docker config
EXPOSE 4505
EXPOSE 4506
CMD ["/usr/bin/supervisord", "-n", "-c", "/etc/supervisor/supervisord.conf"]