FROM hookbrother/phabricator
MAINTAINER hookbrother <hookbrother@gmail.com>

# 环境变量
ENV MYSQL_USER admin
ENV MYSQL_PASS 11111111

ENV PHABRICATOR_HOST dev.hookbrother.net

ENV SMTP_HOST none
ENV SMTP_USER none
ENV SMTP_PASS none
ENV SMTP_PORT 465
ENV SMTP_PROTOCOL SSL

# 安装软件(java maven yarn tomcat)
RUN yum install -y java maven curl tomcat docker-client && \
    curl --silent --location https://rpm.nodesource.com/setup_10.x | bash - && \
    yum -y install nodejs && \
    curl --silent --location https://dl.yarnpkg.com/rpm/yarn.repo | tee /etc/yum.repos.d/yarn.repo && \
    yum install -y yarn

RUN mkdir /root/tmp && \
    cd /root/tmp && \
    wget http://www.sonatype.org/downloads/nexus-latest.war && \
    wget http://mirrors.jenkins-ci.org/war/latest/jenkins.war && \
    mv nexus-latest.war /usr/share/tomcat/webapps/nexus.war && \
    mv jenkins.war /usr/share/tomcat/webapps/jenkins.war && \
    yum clean all && \
    rm -rf var/cache/yum

COPY dev.conf /etc/nginx/conf.d/dev.conf
COPY settings.xml /etc/maven/settings.xml
COPY run.sh /run.sh
RUN chmod 755 /*.sh

VOLUME ["/root/sonatype-work", "/root/.jenkins"]

ENTRYPOINT ["/run.sh"]