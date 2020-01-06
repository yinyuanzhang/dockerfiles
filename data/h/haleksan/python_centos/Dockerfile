FROM centos
RUN yum update -y \
    && yum groupinstall -y "development tools" \
    && yum install -y initscripts openssh-server \
    && ssh-keygen -t rsa -N "" -f ~/.ssh/id_rsa \
    && sshd-keygen -t rsa -N "" -f /etc/ssh/ssh_host_rsa_key \
    && cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys \
    && chmod 0600 ~/.ssh/authorized_keys \
    && cat /etc/ssh/ssh_host_rsa_key.pub >> ~/.ssh/known_hosts \
    && echo "StrictHostKeyChecking no" >> ~/.ssh/config \
    && sed -i 's/.*PermitRootLogin yes/PermitRootLogin yes/' /etc/ssh/sshd_config \
    && sed -i 's/.*#PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config \
    && yum install -y https://centos7.iuscommunity.org/ius-release.rpm  python-devel \
    && yum install -y python36u \
    && alias python3=/usr/bin/python3.6 \
    && curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py" \
    && python get-pip.py \
    && pip install ConfigParser dill enum34 gnupg psutil pytest pyyaml requests tox wheel \
    && rm -rfv /var/cache/yum \
    && rm -rfv ~/.cache/pip
