FROM ubuntu:18.04
LABEL MAINTAINER Jostein Austvik Jacobsen <jostein@nlb.no> <http://www.nlb.no/>

# Set working directory to /opt, which is where we will install things
WORKDIR /opt/

# Set locales
RUN apt-get clean && apt-get update && apt-get install -y locales && locale-gen en_GB en_GB.UTF-8
ENV LANG C.UTF-8
ENV LANGUAGE en_GB:en
ENV LC_ALL C.UTF-8

# Install other dependencies
RUN apt-get update && apt-get install -y \
    vim \
    mariadb-client \
    openssh-client

# Set up automatic import of Bibliofil database
COPY src dds-interface
WORKDIR /opt/dds-interface
CMD /opt/dds-interface/loop.sh 3600
