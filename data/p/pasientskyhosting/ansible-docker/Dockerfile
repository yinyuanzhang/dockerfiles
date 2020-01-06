FROM python:3.7-alpine3.8

ENV LANG=en_US.UTF-8
ENV LC_ALL=en_US.UTF-8
ENV LC_LANG=es_ES.UTF-8

RUN apk update \
    && apk add \
      openssh-server-pam=7.7_p1-r3 \ 
      openssh-client=7.7_p1-r3 \
      git=2.18.1-r0 \
      bash=4.4.19-r1 \
      wget=1.19.5-r0 \
      libffi-dev=3.2.1-r4 \
      musl-dev=1.1.19-r10 \
      net-tools=1.60_git20140218-r2 \
      tzdata=2018f-r0 \
      ca-certificates=20171114-r3 \ 
      make=4.2.1-r2 \
      unzip=6.0-r4 \
      mariadb-dev=10.2.15-r0 \
      gcc=6.4.0-r9 \
      outils-md5=0.7-r0 \
      mysql-client=10.2.15-r0 \
    && rm  -rf /tmp/* /var/cache/apk/* 

RUN sed -i -e "s/bin\/ash/bin\/bash/" /etc/passwd
RUN mkdir -p /data
RUN mkdir /var/run/sshd; mkdir /root/.ssh
RUN echo "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIDnqW7OMYvRrymrL1ZfLJ44cBV+f53sVQwX6utYhoeKZ" >> /root/.ssh/authorized_keys

## Customize
RUN pip3 install --upgrade pip
RUN pip3 install setuptools==40.4.3
RUN pip3 install ansible==2.7.1
RUN pip3 install \
      docker-py==1.10.6 \
      netaddr==0.7.19 \
      jmespath==0.9.3 \
      jinja2==2.10 \
      ansible-modules-hashivault==3.9.8 \
      bcrypt==3.1.4 \
      hvac==0.6.4 \
      requests==2.19.1 \
      mysqlclient==1.3.13 \
      passlib==1.7.1 \
      datadog==0.23.0 \
      pyvmomi==6.7.1

COPY ./sshd_config /etc/ssh/sshd_config
COPY ./ssh/* /root/.ssh/
COPY ./entrypoint.sh /entrypoint.sh

WORKDIR /data
VOLUME ["/data"]
EXPOSE 22

ENTRYPOINT ["/entrypoint.sh"]
