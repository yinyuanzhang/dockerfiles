FROM centos/systemd:latest
RUN yum install -y epel-release \
    && yum install -y python-devel python-pip openssl-devel libffi-devel gcc git sudo iproute initscripts
RUN pip install --upgrade pip setuptools \
    && pip install ansible==2.4.3 pycrypto pytest pytest-gitignore pytest-xdist \
    && pip install git+https://github.com/etingof/apacheconfig.git#egg=apacheconfig \
    && pip install -e git+https://github.com/barnabasJ/testinfra.git@apache_config#egg=testinfra
