FROM centos:7.5.1804
MAINTAINER Liqiang Lau<liqianglau@outlook.com>

# Let's get serf
RUN yum update -y -q
RUN yum install -yq build-essential git supervisor unzip
ADD https://releases.hashicorp.com/serf/0.8.1/serf_0.8.1_linux_amd64.zip serf.zip
ADD https://bootstrap.pypa.io/get-pip.py get-pip.py
RUN python get-pip.py
RUN pip install supervisor
RUN unzip serf.zip
RUN rm serf.zip
RUN mv serf /usr/bin/
ADD /start-serf.sh /start-serf.sh
ADD /run.sh /run.sh
ADD /supervisor/supervisord.conf /etc/supervisord.conf
ADD /supervisor/serf.conf /etc/supervisor/conf.d/supervisord-serf.conf
RUN chmod 755 /*.sh

EXPOSE 7946 7373
CMD ["/run.sh"]
