FROM centos:latest

LABEL de.kdac.agent.maintainer = "Claus Böhmer" \
      de.kdac.agent.authors = "eso@bistum-eichstaett.de" \
      de.kdac.agent.url = "https://hub.docker.com/r/kidac/agent" \
      de.kdac.agent.documentation = "https://hub.docker.com/r/kidac/agent" \
      de.kdac.agent.source = "https://github.com/kidac/agent" \
      de.kdac.agent.version = "6.10.3" \
      de.kdac.agent.vendor = "KDAC - https://ews.kdac.de" \
      de.kdac.agent.licenses = "https://httpd.apache.org/docs/2.4/license.html" \
      de.kdac.agent.title = "Atlassian Bamboo Agent (KDAC Version)" \
      de.kdac.agent.description = "Adapted Atlassian Bamboo Agent Dockerfile used by https://ews.kdac.de"

ENV RUN_USER            daemon
ENV RUN_GROUP           daemon

ENV BAMBOO_AGENT_HOME           /var/atlassian/application-data/bamboo-agent
ENV BAMBOO_AGENT_INSTALL_DIR    /opt/atlassian/bamboo-agent
ENV TINI_VERSION                v0.18.0
ENV MAVEN_INSTALL_DIR           /opt/maven
ENV MAVEN_VERSION		3.6.1

VOLUME ["${BAMBOO_AGENT_HOME}"]

WORKDIR $BAMBOO_AGENT_INSTALL_DIR

CMD ["/entrypoint.sh", "console"]
ENTRYPOINT ["/sbin/tini", "--"]

ADD http://monalisa.cern.ch/MONALISA/download/java/jdk-7u80-linux-x64.rpm /jdk-7u80-linux-x64.rpm
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /sbin/tini

COPY entrypoint.sh              /entrypoint.sh
COPY adoptopenjdk.repo /etc/yum.repos.d/adoptopenjdk.repo

RUN yum -y install which git rpm-build adoptopenjdk-8-openj9 adoptopenjdk-11-openj9 \
 && yum localinstall -y /jdk-7u80-linux-x64.rpm \
 && yum clean all \
 && rm -rf /jdk-7u80-linux-x64.rpm \
 && chmod +x /sbin/tini \
 && alternatives --install /usr/bin/java java /usr/java/jdk1.7.0_80/jre/bin/java 100 \
 && alternatives --install /usr/bin/javaws javaws /usr/java/jdk1.7.0_80/jre/bin/javaws 100 \
 && alternatives --install /usr/bin/javac javac /usr/java/jdk1.7.0_80/bin/javac 100 \
 && alternatives --install /usr/bin/jar jar /usr/java/jdk1.7.0_80/bin/jar 100 \
 && alternatives --set java /usr/lib/jvm/adoptopenjdk-8-openj9/bin/java \
 && alternatives --set javac /usr/lib/jvm/adoptopenjdk-8-openj9/bin/javac \
 && alternatives --set javac /usr/lib/jvm/adoptopenjdk-8-openj9/bin/javac

ARG MAVEN_DOWNLOAD_URL=http://mirrors.sonic.net/apache/maven/maven-3/${MAVEN_VERSION}/binaries/apache-maven-${MAVEN_VERSION}-bin.tar.gz

RUN mkdir -p                                ${MAVEN_INSTALL_DIR} \
    && curl -L --silent                     ${MAVEN_DOWNLOAD_URL} | tar -xz -C ${MAVEN_INSTALL_DIR} --strip-components=1 \
    && chown -R ${RUN_USER}:${RUN_GROUP}    ${MAVEN_INSTALL_DIR}

ARG BAMBOO_VERSION=6.10.3
ENV AGENT_JAR=atlassian-bamboo-agent-installer-${BAMBOO_VERSION}.jar
ARG DOWNLOAD_URL=https://downloads.atlassian.com/software/bamboo/downloads/atlassian-bamboo-${BAMBOO_VERSION}.tar.gz

ARG AGENT_JAR_TARGZ_PATH=atlassian-bamboo-${BAMBOO_VERSION}/atlassian-bamboo/admin/agent/${AGENT_JAR}

RUN mkdir -p                                ${BAMBOO_AGENT_INSTALL_DIR} \
    && curl -L --silent                     ${DOWNLOAD_URL} | tar -xz -C ${BAMBOO_AGENT_INSTALL_DIR} --strip-components=4 ${AGENT_JAR_TARGZ_PATH} \
    && chown -R ${RUN_USER}:${RUN_GROUP}    ${BAMBOO_AGENT_INSTALL_DIR}
