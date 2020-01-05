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
    nano \
    mariadb-client \
    openssh-client \
    python3 \
    python3-pip \
    python3-dev \
    python3-mysqldb \
    python3-lxml \
    python3-flask \
    python3-requests \
    python3-psutil \
    default-libmysqlclient-dev

# Install necessary Python modules
RUN pip3 install mysqlclient
RUN pip3 install pyYAML
RUN pip3 install authlib
RUN pip3 install xmltodict
RUN pip3 install pybrake

# Set up automatic generation of recommendations
COPY src book-recommendations
WORKDIR /opt/book-recommendations

CMD /opt/book-recommendations/loop.sh 86400
