FROM uzresk/ansible-serverspec:v2.7.5

LABEL maintainer "uzresk"

# set locale ja_JP.UTF-8, timezone
RUN localedef -v -c -i ja_JP -f UTF-8 ja_JP.UTF-8; echo "";
ENV LANG=ja_JP.UTF-8
RUN rm -f /etc/localtime
RUN ln -fs /usr/share/zoneinfo/Asia/Tokyo /etc/localtime

# install uses lego
RUN yum -y install iproute \
                   unzip \
                   java-1.8.0-openjdk.x86_64 \
                   java-1.8.0-openjdk-devel.x86_64

RUN mkdir -p /etc/ansible
COPY ansible.cfg /etc/ansible/ansible.cfg
ENV ANSIBLE_CONFIG /etc/ansible/ansible.cfg
