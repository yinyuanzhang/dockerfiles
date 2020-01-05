# The basic image to run Blended containers
FROM atooni/base-alpine:1.0.1

MAINTAINER Andreas Gies 

ENV JAVA_URL=https://cdn.azul.com/zulu/bin/zulu8.38.0.13-ca-jdk8.0.212-linux_musl_x64.tar.gz
ENV SBT_URL=https://piccolo.link/sbt-1.2.8.tgz

# Installation section
ADD files/profile.d /etc/profile.d  

# Download the tar files and explode them in one go to save 
# image space 
RUN mkdir -p /opt \
 && curl -L ${JAVA_URL} | tar -xzC /opt \
 && ln -s $(ls -d /opt/zulu*) /opt/java 

# End of Installation section
