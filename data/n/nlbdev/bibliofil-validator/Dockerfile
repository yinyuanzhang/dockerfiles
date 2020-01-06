FROM ubuntu:18.04
LABEL MAINTAINER Jostein Austvik Jacobsen <jostein@nlb.no> <http://www.nlb.no/>

# Set working directory to /opt, which is where we will install things
WORKDIR /opt/

# Set locales
RUN apt-get clean && apt-get update && apt-get install -y locales && locale-gen en_GB en_GB.UTF-8
ENV LANG C.UTF-8
ENV LANGUAGE en_GB:en
ENV LC_ALL C.UTF-8

# Install Java 8
RUN apt-get update && apt-get install -y openjdk-8-jdk

# Install dependencies
RUN apt-get update && apt-get install -y \
    wget \
    rsync \
    python3 \
    python3-pip

RUN pip3 install lxml python-stdnum

RUN mkdir -p /opt/saxon && wget "https://search.maven.org/remotecontent?filepath=net/sf/saxon/Saxon-HE/9.9.0-2/Saxon-HE-9.9.0-2.jar" -O /opt/saxon/saxon.jar

COPY src bibliofil-validator
WORKDIR /opt/bibliofil-validator

CMD /opt/bibliofil-validator/loop.sh 60
