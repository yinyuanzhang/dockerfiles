FROM nettematic/php:7.0

RUN apt-get update
RUN apt-get install --no-install-recommends -y \
   openssh-server \
   git \ 
   openjdk-8-jre
RUN apt-get clean


ARG user=jenkins
ARG group=jenkins
ARG uid=10000
ARG gid=10000
ARG JENKINS_AGENT_HOME=/home/${user}

ENV JENKINS_AGENT_HOME ${JENKINS_AGENT_HOME}
RUN groupadd -g ${gid} ${group} \
    && useradd -d "${JENKINS_AGENT_HOME}" -u "${uid}" -g "${gid}" -m -s /bin/bash "${user}"

# setup SSH server
RUN sed -i 's/#PermitRootLogin.*/PermitRootLogin no/' /etc/ssh/sshd_config
RUN sed -i 's/#RSAAuthentication.*/RSAAuthentication yes/' /etc/ssh/sshd_config
RUN sed -i 's/#PasswordAuthentication.*/PasswordAuthentication no/' /etc/ssh/sshd_config
RUN sed -i 's/#SyslogFacility.*/SyslogFacility AUTH/' /etc/ssh/sshd_config
RUN sed -i 's/#LogLevel.*/LogLevel INFO/' /etc/ssh/sshd_config
RUN mkdir /var/run/sshd

VOLUME "${JENKINS_AGENT_HOME}" "/tmp" "/run" "/var/run"
WORKDIR "${JENKINS_AGENT_HOME}"

COPY setup-sshd /usr/local/bin/setup-sshd

EXPOSE 22

ENTRYPOINT ["setup-sshd"]
