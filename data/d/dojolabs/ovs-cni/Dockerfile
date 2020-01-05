FROM centos:centos7

# Add everything
ADD . /usr/src/ovs-cni

ENV INSTALL_PKGS "git golang"
RUN rpm --import https://mirror.go-repo.io/centos/RPM-GPG-KEY-GO-REPO && \
    curl -s https://mirror.go-repo.io/centos/go-repo.repo | tee /etc/yum.repos.d/go-repo.repo && \
    yum install -y $INSTALL_PKGS && \
    rpm -V $INSTALL_PKGS && \
    cd /usr/src/ovs-cni && \
    ./build && \
    cp bin/plugin /ovs && \
    yum autoremove -y $INSTALL_PKGS && \
    yum clean all && \
    rm -rf /tmp/*

CMD ["sh", "-c", "cp /ovs /host/opt/cni/bin/ovs && sleep infinity"]
