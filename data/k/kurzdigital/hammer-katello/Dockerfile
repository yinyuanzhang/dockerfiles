from centos:7

RUN yum -y install \
    https://yum.theforeman.org/releases/1.18/el7/x86_64/foreman-release.rpm \
    http://fedorapeople.org/groups/katello/releases/yum/3.7/katello/el7/x86_64/katello-repos-latest.rpm \
    http://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm \
    centos-release-scl.noarch
RUN yum -y install \
    tfm-rubygem-hammer_cli_katello.noarch \
    tfm-rubygem-hammer_cli_foreman_remote_execution.noarch \
    jq \
    && yum clean all
