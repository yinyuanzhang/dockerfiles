FROM centos:6

USER root

RUN yum update -y

RUN yum install -y wget xz

RUN wget https://nodejs.org/dist/v10.13.0/node-v10.13.0-linux-x64.tar.xz

RUN xz -d node-v10.13.0-linux-x64.tar.xz

RUN tar -xf node-v10.13.0-linux-x64.tar

RUN cp -rf node-v10.13.0-linux-x64/* /usr/

RUN curl --silent --location https://dl.yarnpkg.com/rpm/yarn.repo | tee /etc/yum.repos.d/yarn.repo

RUN curl --silent --location https://rpm.nodesource.com/setup_8.x | bash -

RUN yum install -y http://opensource.wandisco.com/centos/6/git/x86_64/wandisco-git-release-6-1.noarch.rpm

RUN yum install -y yarn git

RUN rm -rf node-v10.13.0-linux-x64.tar node-v10.13.0-linux-x64
