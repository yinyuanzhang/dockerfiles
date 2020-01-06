FROM amd64/busybox
LABEL maintainer "Andrey Zhereshchin <andreyzh@ie.ibm.com>"

ARG CHANNEL=stable
ARG VERSION=14.5.33

RUN wget "http://packages.chef.io/files/${CHANNEL}/chef/${VERSION}/el/7/chef-${VERSION}-1.el7.x86_64.rpm" -O /tmp/chef-client.rpm && \
    rpm2cpio /tmp/chef-client.rpm | cpio -idm && \
    rm -rf /tmp/chef-client.rpm

VOLUME [ "/opt/chef" ]
