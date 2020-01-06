# Copyright 2019 The Ubuntu APT Mirror Docker
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# imitations under the License.

FROM ubuntu:18.04

MAINTAINER bdy1234567@126.com

# docker build -t dybai/apt-mirror:1.0 .
# docker run -d -v /home/dybai/docker/apt-mirror/data:/data -p 12345:80 -p 12346:8080 dybai/apt-mirror:1.0
# docker start [CONTAINER ID]
# docker exec -it [CONTAINER ID] /bin/bash

# Set default timezone, Quietly install tzdata.
ENV DEBIAN_FRONTEND noninteractive

# Install dependent packages.
RUN apt-get update
RUN apt-get install -y --assume-yes apt-utils
RUN apt-get dist-upgrade -y --assume-yes
RUN apt-get install -y --assume-yes vim net-tools tzdata
RUN apt-get install -y --assume-yes apt-mirror apache2 nginx cron
RUN apt-get clean

# Modify timezone.
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
# Make timezone settings effective.
RUN dpkg-reconfigure -f noninteractive tzdata

# [FIXME] Can't use the $HOME environment variable at here?
COPY mk.sh /root
COPY sync.sh /root
COPY run.sh /root

RUN /bin/chmod a+x ${HOME}/mk.sh
RUN /bin/chmod a+x ${HOME}/sync.sh
RUN /bin/chmod a+x ${HOME}/run.sh

COPY apt/mirror.list.18.04 /etc/apt
COPY apt/mirror.list.16.04 /etc/apt
COPY apt/mirror.list.14.04 /etc/apt

COPY apache2/000-default.conf /etc/apache2/sites-available/000-default.conf
COPY apache2/apache2.conf /etc/apache2/apache2.conf
COPY apache2/ports.conf /etc/apache2/ports.conf

COPY nginx/nginx.conf /etc/nginx/nginx.conf
COPY nginx/default /etc/nginx/sites-available/default

RUN /bin/echo '0 2 * * * /root/sync.sh' >> /var/spool/cron/crontabs/root
RUN /bin/chmod 600 /var/spool/cron/crontabs/root
RUN /bin/chown root:crontab /var/spool/cron/crontabs/root

RUN /bin/bash -c /root/mk.sh

CMD /bin/bash -c ${HOME}/run.sh
