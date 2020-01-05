FROM centos:7

RUN yum install git -y
WORKDIR /root
RUN git clone git://github.com/ansible/ansible.git && source /root/ansible/hacking/env-setup
RUN curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py" && python get-pip.py
RUN pip install ansible

ENV source /root/ansible/hacking/env-setup
ENV PATH=/root/ansible/bin:$PATH
