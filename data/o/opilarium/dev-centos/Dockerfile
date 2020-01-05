FROM centos:7
MAINTAINER Michael Rybakov opilar@ya.ru

RUN yum -y update && yum clean all

RUN yum install -y \
    epel-release \
    && yum clean all

RUN yum install -y \
    gcc \
    gcc-c++ \
    make \
    cmake3 \
    zip \
    unzip \
    python-pip \
    git \
    python34 \
    python34-devel \
    which \
    && yum clean all

RUN curl -SL https://github.com/ninja-build/ninja/releases/download/v1.7.1/ninja-linux.zip > /tmp/ninja.zip \
    && unzip /tmp/ninja.zip -d /usr/bin \
    && rm /tmp/ninja.zip

RUN ln -s /usr/bin/cmake3 /usr/bin/cmake

RUN pip install conan==0.16.1
RUN conan --version