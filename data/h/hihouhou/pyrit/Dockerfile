#
# Pyrit Dockerfile
#
# https://github.com/
#

# Pull base image.
FROM debian:latest

MAINTAINER hihouhou < hihouhou@hihouhou.com >

ENV PYRIT_VERSION pyrit-0.3.0

# Update & install packages for Pyrit
RUN apt-get update && \
    apt-get install -y wget libssl-dev python-dev zlib1g-dev gcc

#Get Pyrit
RUN wget http://pyrit.googlecode.com/files/${PYRIT_VERSION}.tar.gz && \
    tar xvf ${PYRIT_VERSION}.tar.gz

#Compiling Pyrit
RUN cd $PYRIT_VERSION && \
    python setup.py build && \
    python setup.py install

CMD ["/bin/bash"]
