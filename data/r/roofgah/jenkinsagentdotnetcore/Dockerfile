FROM mcr.microsoft.com/dotnet/core/sdk:3.0.100-alpine3.9

#Install git openssh curl bash and java
RUN set -ex && apk add --no-cache git openssh-client curl bash openjdk8-jre

#Add jenkins user
ARG user=jenkins
ARG group=jenkins
RUN addgroup -S ${group}
RUN adduser -S ${user} -G ${group}
ARG AGENT_WORKDIR=/home/${user}/agent
USER ${user}
ENV AGENT_WORKDIR=${AGENT_WORKDIR}
RUN mkdir /home/${user}/.jenkins && mkdir -p ${AGENT_WORKDIR}

VOLUME /home/${user}/.jenkins
VOLUME ${AGENT_WORKDIR}
WORKDIR /home/${user}

USER root
ARG JENKINS_URL=https://repo.jenkins-ci.org/public/org/jenkins-ci/main/remoting/3.9/remoting-3.9.jar  
RUN mkdir /usr/share/jenkins/
RUN curl -fsSL ${JENKINS_URL} -o /usr/share/jenkins/agent.jar

COPY jenkins-agent /usr/local/bin/jenkins-agent
RUN chmod +x /usr/local/bin/jenkins-agent &&\
    ln -s /usr/local/bin/jenkins-agent /usr/local/bin/jenkins-slave
USER ${user}

ENTRYPOINT ["jenkins-slave"]