FROM ubuntu:16.04
MAINTAINER Shawn Dempsay <shawn@dempsay.org>

## 
## Put apt into non-interactive mode
##
ENV DEBIAN_FRONTEND noninteractive 

##
# Set up Open JDK8
#
RUN apt-get update && apt-get install -y openjdk-8-jre-headless openjdk-8-jdk-headless
RUN java -version
