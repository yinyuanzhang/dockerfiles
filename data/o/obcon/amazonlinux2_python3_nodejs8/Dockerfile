FROM amazonlinux:2

RUN yum -y update

RUN yum -y install python3
RUN pip3 install awscli pipenv

RUN curl --silent --location https://rpm.nodesource.com/setup_8.x | bash -
RUN yum -y install nodejs
