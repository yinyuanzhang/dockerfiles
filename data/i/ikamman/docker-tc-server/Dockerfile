FROM dockerfile/java:oracle-java8

MAINTAINER Kamil Manka <kamil.manka@gmail.com>

# TeamCity data directory
VOLUME  ["/data/teamcity"]
ENV TEAMCITY_DATA_PATH /data/teamcity

# Download and install TeamCity to /opt
RUN apt-get -y install tar wget
ENV TEAMCITY_VERSION 9.0.1
ENV TEAMCITY_PACKAGE TeamCity-$TEAMCITY_VERSION.tar.gz
RUN echo $TEAMCITY_PACKAGE
ENV TEAMCITY_DOWNLOAD http://download-cf.jetbrains.com/teamcity
RUN wget -qO- $TEAMCITY_DOWNLOAD/$TEAMCITY_PACKAGE | tar xz -C /opt

EXPOSE 8111
CMD ["/opt/TeamCity/bin/teamcity-server.sh", "run"]