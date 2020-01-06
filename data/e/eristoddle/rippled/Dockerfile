FROM ubuntu:18.04

# Official instructions from
# https://ripple.com/build/rippled-setup/#installation-on-ubuntu-with-alien
RUN apt-get update
RUN apt-get install -y yum-utils alien
RUN rpm -Uvh https://mirrors.ripple.com/ripple-repo-el7.rpm
RUN yumdownloader --enablerepo=ripple-stable --releasever=el7 rippled
RUN rpm --import https://mirrors.ripple.com/rpm/RPM-GPG-KEY-ripple-release && rpm -K rippled*.rpm
RUN alien -i --scripts rippled*.rpm && rm rippled*.rpm

COPY ./rippled.cfg /opt/ripple/etc/rippled.cfg

ENTRYPOINT ["/opt/ripple/bin/rippled"]
