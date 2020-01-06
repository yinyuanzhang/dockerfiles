FROM centos:7

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

RUN rpm --import https://repos.azul.com/azul-repo.key && \
    curl -o /etc/yum.repos.d/zing.repo https://repos.azul.com/zing/rhel/zing.repo && \
    yum install -y zing-jdk1.8.0-19.07.0.0-4
