FROM amazonlinux:with-sources
MAINTAINER Marc Rosenthal <marc@affordabletours.com>

RUN yum update -y
RUN yum -y install xz git openssh-clients bzip2 gcc-c++

# add nodejs repo
RUN curl --silent --location https://rpm.nodesource.com/setup_10.x | bash -
RUN yum -y install nodejs

# update npm to latest version
RUN npm install -g npm

RUN curl -O https://bootstrap.pypa.io/get-pip.py
RUN python get-pip.py --user
ENV PATH /root/.local/bin:$PATH
RUN pip install awsebcli --upgrade --user
RUN yum -y install git
