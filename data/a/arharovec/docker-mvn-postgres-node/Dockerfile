FROM atlassian/default-image

MAINTAINER Serhii S

# this is a non-interactive automated build - avoid some warning messages
ENV DEBIAN_FRONTEND noninteractive

###===================    MAVEN    ===================#
# delete old version 
RUN apt-get purge -y maven

# get maven 3.3.9
RUN wget --no-verbose -O /tmp/apache-maven-3.3.9.tar.gz http://apache.cp.if.ua/maven/maven-3/3.3.9/binaries/apache-maven-3.3.9-bin.tar.gz

# verify checksum
RUN echo "516923b3955b6035ba6b0a5b031fbd8b /tmp/apache-maven-3.3.9.tar.gz" | md5sum -c

# install maven
RUN tar xzf /tmp/apache-maven-3.3.9.tar.gz -C /opt/
RUN ln -s /opt/apache-maven-3.3.9 /opt/maven
RUN ln -s /opt/maven/bin/mvn /usr/local/bin
RUN rm -f /tmp/apache-maven-3.3.9.tar.gz
ENV MAVEN_HOME /opt/maven

#===================    PostgreSQL     ===================# 
# install PostgreSQL 
RUN add-apt-repository "deb http://apt.postgresql.org/pub/repos/apt/ precise-pgdg main" \
  && wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - \
  && apt-get update \
  && apt-get install -y postgresql-9.6 

#===================    Finalization     ===================# 
# remove download archive files
RUN apt-get clean \
  && apt-get install sudo \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

#END OF CONFIG