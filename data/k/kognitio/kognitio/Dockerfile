FROM centos:centos7

ARG kognitio_version=80204rel191024
ARG kognitio_download=https://releases.kognitio.com/wx2/wx2-${kognitio_version}.tgz

ADD https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm /tmp/epel.noarch.rpm
ADD ${kognitio_download} /tmp/kognitio.tgz

RUN yum install -y /tmp/epel.noarch.rpm; \
    yum update ;\
    yum install -y net-tools bind-utils perl python zlib openssl tar gzip sudo libcgroup-tools java-1.8.0-openjdk-headless python-pip python36 python36-pip ;\
    pip install numpy==1.16.5 scipy==1.2.2 ;\
    pip3 install numpy scipy


RUN useradd -d /home/kognitio.admin -m -c "Kognitio Admin User" kognitio.admin ;\
    mkdir -p /opt/kognitio ;\
    chown kognitio.admin:kognitio.admin /opt/kognitio ;\
    mkdir -p /data/dfs ;\
    mkdir -p /data/config ;\
    mkdir -p /data/nodes ;\
    chown -R kognitio.admin:kognitio.admin /data ;\
    mkdir /home/kognitio.admin/.ssh ;\
    chown -R kognitio.admin:kognitio.admin /home/kognitio.admin ;\
    chmod 644 /tmp/kognitio.tgz ;\
    echo "kognitio.admin ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers


ADD scripts /opt/kognitio/scripts

COPY LICENSE /opt/kognitio
COPY README /opt/kognitio

RUN sudo -u kognitio.admin tar -C /tmp -xzf /tmp/kognitio.tgz;\
    sudo -u kognitio.admin /tmp/wxinstaller-${kognitio_version} -p /tmp/wx2-${kognitio_version}.wxpkg -S kognitio -m - -a - -n all -t full -O install_root=/opt/kognitio/wx2 -O accept_eula=yes -u -C ;\
    sudo -u kognitio.admin rm -f /tmp/wxinstaller-${kognitio_version} /tmp/wx2-${kognitio_version}.wxpkg ;\
    rm -f /tmp/kognitio.tgz ;\
    sudo -u kognitio.admin /opt/kognitio/wx2/current/bin/wxconftool -l -s system -a partitions= -W ;\
    sudo -u kognitio.admin /opt/kognitio/wx2/current/bin/wxconftool -l -s system -a memsize=\`/opt/kognitio/scripts/memory-size\` -W ;\
    sudo -u kognitio.admin /opt/kognitio/wx2/current/bin/wxconftool -l -s network -a "regcmd=/opt/kognitio/scripts/register-wx2 /data/nodes" -W


EXPOSE 6550

WORKDIR /home/kognitio.admin

USER kognitio.admin

ENV PATH /opt/kognitio/scripts:/opt/kognitio/wx2/current/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

ENTRYPOINT /opt/kognitio/scripts/kognitio-entrypoint

VOLUME /data

                
