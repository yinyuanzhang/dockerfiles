FROM circleci/openjdk:8-jdk

LABEL org.label-schema.name = "comms-circleci-base"
LABEL org.label-schema.description = "The circleci base image for comms ovotech team"
LABEL org.label-schema.vcs-url = "https://github.com/ovotech/comms-docker-circleci"
LABEL org.label-schema.vendor = "OVO Energy"

USER root

RUN apt-get update \
	&& apt-get install -y libpython2.7-dev python-pip

RUN pip install awscli credstash==1.14.0

USER circleci

# Smoke tests
RUN pip --version > /dev/null \
	&& aws --version > /dev/null \
	&& credstash -h > /dev/null
