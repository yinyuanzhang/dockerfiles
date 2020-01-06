FROM ubuntu:16.04

MAINTAINER zyt

RUN apt-get update && apt-get install -y supervisor python-setuptools python-pip

CMD ["supervisord", "-n","-c", "/etc/supervisor/conf.d/supervisord.conf"]
