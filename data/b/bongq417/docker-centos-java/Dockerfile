FROM centos:latest

ARG JAVA_VERSION=8

RUN yum -y install "java-1.$JAVA_VERSION.0-openjdk" && \
    yum -y install kde-l10n-Chinese && \
    yum -y install less vim nano && \
    yum -y reinstall glibc-common && \
    yum clean all && \
    localedef -c -f UTF-8 -i zh_CN zh_CN.utf8 && \
    rm -rf /var/cache/yum && \
    /bin/cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    echo 'Asia/Shanghai' >/etc/timezone

ENV LANG zh_CN.UTF-8

CMD ["/bin/bash"]