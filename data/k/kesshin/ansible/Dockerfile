FROM ubuntu:trusty
MAINTAINER Simone Bembi <simone.bembi@gmail.com>

ENV TERM=xterm-256color

RUN apt-get update -qy && \
	apt-get install -qy software-properties-common && \
	apt-add-repository -y ppa:ansible/ansible && \
	apt-get update -qy && \
	apt-get install -qy ansible

VOLUME /ansible
WORKDIR /ansible

ENTRYPOINT ["ansible-playbook"]
CMD ["site.yml"]