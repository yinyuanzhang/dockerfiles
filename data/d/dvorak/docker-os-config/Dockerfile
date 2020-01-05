FROM fedora:23

RUN dnf install -y git iproute python-pip redhat-lsb \
  && dnf clean all

RUN git clone --branch master --depth=1 \
  https://github.com/openstack-dev/devstack

RUN ln /usr/bin/env /usr/bin/sudo 

RUN cd devstack \
  && tools/install_prereqs.sh \
  && dnf clean all

RUN pip install -U pip \
  && pip install virtualenv \
  && virtualenv /venv
