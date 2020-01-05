FROM ubuntu:14.04

# environment
ENV DEBIAN_FRONTEND noninteractive

# required packages for td-agent
RUN apt-get update && apt-get install -y \
    curl \
    libcurl4-openssl-dev \
    ruby \
    ruby-dev \
    make

# install fluentd td-agent
ADD ./pkg/td-agent_2.2.0-0_amd64.deb /tmp/td-agent_2.2.0-0_amd64.deb
RUN dpkg -i /tmp/td-agent_2.2.0-0_amd64.deb
RUN apt-get install -f

# clean cache files
#RUN apt-get clean && rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*

# stop running fluentd
RUN /etc/init.d/td-agent stop

# base configuration
COPY ./config/fluent.conf /etc/fluentd/fluent.conf

ENTRYPOINT ["/opt/td-agent/embedded/bin/fluentd"]
CMD ["-c","/etc/fluentd/fluent.conf"]