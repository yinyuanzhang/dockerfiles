##
# NAME             :
# VERSION          : 1.0
# DOCKER-VERSION   : 1.12
# DESCRIPTION      : A container with node and sonar to execute sonar analysis
# TO_BUILD         : docker build --pull=true --no-cache --rm -t adrienpessu/docker-node-sonar:master . && docker tag adrienpessu/docker-node-sonar:master adrienpessu/docker-node-sonar:1.1 && docker tag adrienpessu/docker-node-sonar:1.1 adrienpessu/docker-node-sonar:latest
# TO_RUN           : docker run -it --volume=/Users/adrien/workspaces/kconnect/app-service:/localDebugRepo --workdir="/localDebugRepo" --memory=4g --entrypoint=/bin/bash adrienpessu/docker-node-sonar
##


# extend the most recent long term support Ubuntu version
FROM node:7.7.1

MAINTAINER Adrien PESSU

# set shell variables for java installation
ENV java_version 1.8.0_11
ENV filename jdk-8u11-linux-x64.tar.gz
ENV downloadlink http://download.oracle.com/otn-pub/java/jdk/8u11-b12/$filename

# download java, accepting the license agreement
RUN wget --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie" -O /tmp/$filename $downloadlink

# unpack java
RUN mkdir /opt/java-oracle && tar -zxf /tmp/$filename -C /opt/java-oracle/
ENV JAVA_HOME /opt/java-oracle/jdk$java_version
ENV PATH $JAVA_HOME/bin:$PATH

RUN apt-get update && apt-get install -y unzip

# configure symbolic links for the java and javac executables
RUN update-alternatives --install /usr/bin/java java $JAVA_HOME/bin/java 20000 && update-alternatives --install /usr/bin/javac javac $JAVA_HOME/bin/javac 20000

RUN wget -O /tmp/sonar-scanner-2.8.zip "https://sonarsource.bintray.com/Distribution/sonar-scanner-cli/sonar-scanner-2.8.zip" \
    && unzip /tmp/sonar-scanner-2.8.zip -d /etc/lib/ \
    && rm /tmp/sonar-scanner-2.8.zip \
    && ln -s /etc/lib/sonar-scanner-2.8//bin/sonar-scanner /usr/local/bin/sonar-scanner

CMD [ "node" ]