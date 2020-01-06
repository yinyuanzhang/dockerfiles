FROM debian:stretch-slim
MAINTAINER Romain THERRAT

ENV DEBIAN_FRONTEND noninteractive

# Install deps and create shinken user
RUN apt-get update && apt-get install -y --no-install-recommends python-pycurl python-setuptools python-cherrypy3 python-crypto monitoring-plugins-standard ca-certificates host && \
    easy_install pip && \
    useradd shinken && \
    apt-get -y autoremove && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install shinken
RUN pip install shinken==2.4.3 && \
    shinken --init && \
    rm -r /var/lib/shinken/doc/*

ADD shinken.cfg /etc/shinken/shinken.cfg
ADD brokerd.ini /etc/shinken/daemons/brokerd.ini
ADD pollerd.ini /etc/shinken/daemons/pollerd.ini
ADD schedulerd.ini /etc/shinken/daemons/schedulerd.ini
ADD reactionnerd.ini /etc/shinken/daemons/reactionnerd.ini
ADD receiverd.ini /etc/shinken/daemons/receiverd.ini

COPY launch.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/launch.sh

ENTRYPOINT ["/usr/local/bin/launch.sh"]
