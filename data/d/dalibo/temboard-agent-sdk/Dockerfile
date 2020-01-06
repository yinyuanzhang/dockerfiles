FROM centos:7

ADD https://github.com/vishnubob/wait-for-it/raw/master/wait-for-it.sh /usr/local/bin/
RUN set -ex; \
    chmod +x /usr/local/bin/wait-for-it.sh; \
    sed -i s/^keepcache=.*/keepcache=1/ /etc/yum.conf; \
    rpm --import \
        https://yum.postgresql.org/RPM-GPG-KEY-PGDG-11 \
        https://yum.postgresql.org/RPM-GPG-KEY-PGDG-10 \
        https://yum.postgresql.org/RPM-GPG-KEY-PGDG-94 \
        https://yum.postgresql.org/RPM-GPG-KEY-PGDG-95 \
        https://yum.postgresql.org/RPM-GPG-KEY-PGDG-96 \
    ; \
    yum -q -y install \
        epel-release \
        https://download.postgresql.org/pub/repos/yum/11/redhat/rhel-7-x86_64/pgdg-centos11-11-2.noarch.rpm \
        https://download.postgresql.org/pub/repos/yum/10/redhat/rhel-7-x86_64/pgdg-centos10-10-2.noarch.rpm \
        https://download.postgresql.org/pub/repos/yum/9.6/redhat/rhel-7-x86_64/pgdg-centos96-9.6-3.noarch.rpm \
        https://download.postgresql.org/pub/repos/yum/9.5/redhat/rhel-7-x86_64/pgdg-centos95-9.5-3.noarch.rpm \
        https://download.postgresql.org/pub/repos/yum/9.4/redhat/rhel-7-x86_64/pgdg-centos94-9.4-3.noarch.rpm \
    ; \
    yum -q -y install \
        postgresql11-server postgresql11-contrib \
        postgresql10-server postgresql10-contrib \
        postgresql96-server postgresql96-contrib \
        postgresql95-server postgresql95-contrib \
        postgresql94-server postgresql94-contrib \
    ; \
    yum clean all ; \
    :

RUN set -ex; \
    yum -q -y install \
        git \
        less \
        make \
        net-tools \
        openssl \
        procps-ng \
        psmisc \
        python2-pip \
        python-setuptools \
        rpm-build \
        rsync \
        sudo \
        yum-utils \
    ; \
    yum clean all ; \
    yum makecache fast; \
    :

ADD https://github.com/krallin/tini/releases/download/v0.18.0/tini /usr/local/sbin/tini

RUN set -ex; \
    chmod +x /usr/local/sbin/tini; \
    pip install "pytest"; \
    rm -rf ~/.cache/; \
    useradd --system testuser; \
    :

ENTRYPOINT ["/usr/local/sbin/tini", "-gw", "--"]
