FROM centos:7.6.1810

MAINTAINER ellios <104082492@qq.com>

# basic settings
ENV TZ=Asia/Shanghai \
    LANG=en_US.UTF-8 

RUN ln -sf /usr/share/zoneinfo/${TZ} /etc/localtime

# basic paths
ENV TOP_HOME=/var/www
ENV APP_HOME=${TOP_HOME}/app \
    LOG_DIR=${TOP_HOME}/logs

RUN set -x && chmod a+x root && mkdir -p ${APP_HOME} ${LOG_DIR}

# basic tools
RUN set -x && yum -y install wget unzip net-tools sysstat lrzsz && yum clean all

# jdk

ENV JAVA_DOWNLOAD_URL="http://download.oracle.com/otn-pub/java/jdk/8u201-b09/42970487e3af4f5aa5bca3f542482c60/jdk-8u201-linux-x64.rpm" \
 JAVA_HOME=/usr/java/latest

RUN wget -q --no-cookies --no-check-certificate --header "Cookie: oraclelicense=accept-securebackup-cookie" ${JAVA_DOWNLOAD_URL} -O /tmp/java.rpm \
 && yum -y install /tmp/java.rpm \
 && yum clean all \
 && rm -rf /tmp/*

# sshd
RUN set -x \
 && yum install -y openssh-server openssh-clients \
 && ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key \
 && ssh-keygen -t ecdsa -f /etc/ssh/ssh_host_ecdsa_key \
 && ssh-keygen -t ed25519 -f /etc/ssh/ssh_host_ed25519_key \
 && yum clean all

EXPOSE 22 80 8080 8500

CMD ["/usr/sbin/sshd", "-D"]