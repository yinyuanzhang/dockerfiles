FROM centos:7.4.1708

LABEL  maintainer "Hitoshi Hayakawa <hykw1234@gmail.com>"

RUN yum -y update && \
    yum -y reinstall glibc-common && \
    yum clean all && \
    /bin/cp -f /usr/share/zoneinfo/Asia/Tokyo /etc/localtime

# needing ja locales, don't call before 'yum reinstall glibc-common'
ENV LANG="ja_JP.UTF-8" \
    LANGUAGE="ja_JP:ja" \
    LC_ALL="ja_JP.UTF-8"

RUN \
  localedef -f UTF-8 -i ja_JP ja_JP.UTF-8 && \
  yum install -y ansible && \
  yum install -y openssh-clients && \
  true
