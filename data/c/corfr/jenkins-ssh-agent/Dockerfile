# The MIT License
#
#  Copyright (c) 2015, CloudBees, Inc.
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#  THE SOFTWARE.

FROM openjdk:8-jdk
LABEL MAINTAINER="Nicolas De Loof <nicolas.deloof@gmail.com>"

ARG user=jenkins
ARG group=jenkins
ARG uid=1000
ARG gid=1000
ARG JENKINS_AGENT_HOME=/home/${user}

ENV JENKINS_AGENT_HOME ${JENKINS_AGENT_HOME}

RUN groupadd -g ${gid} ${group} \
    && useradd -d "${JENKINS_AGENT_HOME}" -u "${uid}" -g "${gid}" -m -s /bin/bash "${user}"

# setup SSH server
RUN apt-get update \
    && apt-get install --no-install-recommends -y openssh-server \
    && apt-get clean
RUN sed -i 's/#PermitRootLogin.*/PermitRootLogin no/' /etc/ssh/sshd_config
RUN sed -i 's/#RSAAuthentication.*/RSAAuthentication yes/' /etc/ssh/sshd_config
RUN sed -i 's/#PasswordAuthentication.*/PasswordAuthentication no/' /etc/ssh/sshd_config
RUN sed -i 's/#SyslogFacility.*/SyslogFacility AUTH/' /etc/ssh/sshd_config
RUN sed -i 's/#LogLevel.*/LogLevel INFO/' /etc/ssh/sshd_config
RUN sed -ri 's/^session\s+required\s+pam_loginuid.so$/session optional pam_loginuid.so/' /etc/pam.d/sshd
RUN mkdir /var/run/sshd

# Docker version follows stable from CoreOS
ENV DOCKER_VERSION 1.12.6

RUN ( cd /tmp && \
      curl -fsSLO https://get.docker.com/builds/Linux/x86_64/docker-$DOCKER_VERSION.tgz && \
      tar --strip-components=1 -xvzf docker-$DOCKER_VERSION.tgz -C /usr/bin )

# Add static tini
ENV TINI_VERSION v0.14.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini-static /opt/tini/tini
RUN chmod +x /opt/tini/tini
VOLUME /opt/tini
# encaps
RUN ( \
        cd /usr/bin && \
        curl -o master.zip -L https://github.com/swi-infra/jenkins-docker-encaps/archive/master.zip && \
        unzip master.zip && \
        mv jenkins-docker-encaps-master/encaps* . && \
        rm -rf master.zip jenkins-docker-encaps-master \
    )

# Base packages
RUN ( apt-get update && \
      apt-get -y install net-tools git python bzip2 jq netcat-openbsd libxml2-utils rsync && \
      apt-get clean && \
      rm -rf /var/lib/apt/lists/* )

VOLUME "${JENKINS_AGENT_HOME}" "/tmp" "/run" "/var/run"
WORKDIR "${JENKINS_AGENT_HOME}"

COPY setup-sshd /usr/local/bin/setup-sshd

EXPOSE 22

ENTRYPOINT ["/opt/tini/tini","--","/usr/local/bin/setup-sshd"]
