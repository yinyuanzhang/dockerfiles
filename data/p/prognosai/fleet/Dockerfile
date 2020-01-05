FROM ubuntu:trusty
MAINTAINER Ankur Shah <ashah@prognos.ai>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get -q update && \
  apt-get -y -q dist-upgrade && \
  apt-get -y -q install python-setuptools python-pip curl unzip

RUN curl -O https://dl.kolide.co/bin/fleet_latest.zip

RUN unzip fleet_latest.zip 'linux/*' -d fleet && cp fleet/linux/fleet /usr/bin/fleet && rm fleet_latest.zip

RUN curl https://s3.amazonaws.com/aws-cloudwatch/downloads/latest/awslogs-agent-setup.py -o awslogs-agent-setup.py

COPY awslogs.conf awslogs.conf
RUN python ./awslogs-agent-setup.py -n -r us-east-1 -c /awslogs.conf

COPY run.sh run.sh

CMD ["/bin/sh","/run.sh"]
