# Build an Ubuntu 14.04 host with Python v2.7
FROM ubuntu:14.04
MAINTAINER Ash Wilson awilson@cloudpassage.com
    
RUN apt-get update && apt-get upgrade -y && apt-get install -y \
    git-core \
    curl \
    python
                     
RUN apt-get remove -y python3.4
RUN apt-get clean
