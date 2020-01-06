FROM jordan/rundeck:2.11.5
MAINTAINER lbognini@gmail.com

#Install AWS CLI
RUN apt-get update  && apt-get install -y unzip python

RUN curl -O https://bootstrap.pypa.io/get-pip.py  \
    && python get-pip.py --user 

RUN ~/.local/bin/pip install awscli


VOLUME ~/.aws
