FROM centos:7

MAINTAINER "Anooky" <hi@anooky.com>

ENV OC_VERSION "v3.11.0"
ENV OC_RELEASE "openshift-origin-client-tools-v3.11.0-0cbc58b-linux-64bit"

RUN yum install -y \
 ca-certificates \
 git \
 curl \
 which \
 && yum clean all
RUN curl -L https://github.com/openshift/origin/releases/download/$OC_VERSION/$OC_RELEASE.tar.gz | tar -C /usr/local/bin -xzf - --strip-components=1
