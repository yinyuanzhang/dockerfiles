FROM ubuntu:14.04
MAINTAINER Whit Morriss <whit.morriss@canonical.com>

ADD setup.sh /setup.sh
RUN /setup.sh

RUN mkdir /home/ubuntu/.juju
RUN mkdir /home/ubuntu/trusty
RUN mkdir /home/ubuntu/precise

VOLUME ["/home/ubuntu/.juju"]

#ADD patchcontainer.sh /patchcontainer.sh
ADD run.sh /run.sh
ADD cleanup.sh /cleanup.sh
ADD charming-setup.sh /charming-setup.sh

RUN /charming-setup.sh
RUN /cleanup.sh
CMD /run.sh
