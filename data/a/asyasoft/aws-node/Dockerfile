FROM amazonlinux:latest
ENV HOME .
RUN curl -sL https://rpm.nodesource.com/setup_10.x | bash -
RUN yum update -y
RUN yum install -y git nano aws-cli nodejs zip
