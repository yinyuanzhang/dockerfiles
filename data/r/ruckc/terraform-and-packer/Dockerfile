#FROM registry.access.redhat.com/ubi7
FROM fedora:30
RUN yum update -y && yum install unzip ncurses-compat-libs qemu-kvm qemu-img qemu-system-x86 wget -y && yum clean all
ENV PACKER_VERSION=1.4.3 TERRAFORM_VERSION=0.12.6 OVFTOOL_VERSION=4.3.0-12320924
RUN wget -nv -P /root https://releases.hashicorp.com/packer/${PACKER_VERSION}/packer_${PACKER_VERSION}_linux_amd64.zip && \
    unzip /root/packer_${PACKER_VERSION}_linux_amd64.zip -d /usr/local/bin && \
    rm -vf /root/packer_${PACKER_VERSION}_linux_amd64.zip && \
    wget -nv -P /root https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip && \
    unzip /root/terraform_${TERRAFORM_VERSION}_linux_amd64.zip -d /usr/local/bin && \
    rm -vf /root/terraform_${TERRAFORM_VERSION}_linux_amd64.zip
# ovftool disabled because its not in use at the moment
# && \
#    wget -nv -P /root https://ci.ruck.io/nexus/repository/raw/vmware/VMware-ovftool-${OVFTOOL_VERSION}-lin.x86_64.bundle && \
#    /bin/sh /root/VMware-ovftool-${OVFTOOL_VERSION}-lin.x86_64.bundle -p /usr/local --console --eulas-agreed --required && \
#    rm -vf /root/VMware-ovftool-${OVFTOOL_VERSION}-lin.x86_64.bundle
