FROM ubuntu:xenial
	
ARG JENKINS_VERSION
ENV JENKINS_VERSION ${JENKINS_VERSION:-2.19.1}

ARG DOCKER_VERSION
ENV DOCKER_VERSION ${DOCKER_VERSION:-1.12.1}

ARG user=jenkins
ARG uid=1000

ARG group=jenkins
ARG gid=1000

ENV JENKINS_HOME /jenkins_home
ENV JENKINS_SLAVE_AGENT_PORT 50000


#RUN apt-get clean && echo "deb http://ftp.ca.debian.org/debian/ jessie main" > /etc/apt/sources.list.d/main.list && apt-get update -qq

RUN apt-get update && \

apt-get install -qqy --force-yes \
	sudo \
    apt-transport-https \
    openjdk-8-jdk-headless \
    git \
    rsync \
    zip \
    ca-certificates \
    curl \
    python-dev \
    python-setuptools \
    libyaml-dev \
    python-pip \
    xvfb \
    python-rpm \
    yum \
    libssl-dev \
    libffi-dev \
    lxc \
    iptables \
    supervisor && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get clean autoclean && \
    apt-get autoremove -y && \
    rm -rf /var/lib/{apt,dpkg,cache,log}/ 

# RUN pip install --user --upgrade https://github.com/anchore/anchore/zipball/master

RUN curl -sSL https://get.docker.com/builds/Linux/x86_64/docker-$DOCKER_VERSION.tgz | tar xvz \
	&& mv ./docker/* /usr/bin

ADD ./wrapdocker /usr/local/bin/wrapdocker
RUN chmod +x /usr/local/bin/wrapdocker



# Jenkins is run with user `jenkins`, uid = 1000
# If you bind mount a volume from the host or a data container, 
# ensure you use the same uid
RUN groupadd -g ${gid} ${group} \
    && useradd -d "$JENKINS_HOME" -u ${uid} -g ${gid} -m -s /bin/bash ${user} \
    && groupadd docker \
    && echo "jenkins:jenkins" | chpasswd  && echo "jenkins ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers && usermod -a -G docker jenkins

VOLUME /jenkins_home

# `/usr/share/jenkins/ref/` contains all reference configuration we want 
# to set on a fresh new installation. Use it to bundle additional plugins 
# or config file with your custom jenkins Docker image.
RUN mkdir -p /usr/share/jenkins/ref/init.groovy.d

ENV TINI_SHA 066ad710107dc7ee05d3aa6e4974f01dc98f3888

# Use tini as subreaper in Docker container to adopt zombie processes 
RUN curl -fsSL https://github.com/krallin/tini/releases/download/v0.5.0/tini-static -o /bin/tini && chmod +x /bin/tini \
  && echo "$TINI_SHA  /bin/tini" | sha1sum -c -

COPY init.groovy /usr/share/jenkins/ref/init.groovy.d/tcp-slave-agent-port.groovy

# could use ADD but this one does not check Last-Modified header 
# see https://github.com/docker/docker/issues/8331
RUN curl -fsSL http://repo.jenkins-ci.org/public/org/jenkins-ci/main/jenkins-war/${JENKINS_VERSION}/jenkins-war-${JENKINS_VERSION}.war -o /usr/share/jenkins/jenkins.war

ENV JENKINS_UC https://updates.jenkins.io
RUN chown -R ${user} "$JENKINS_HOME" /usr/share/jenkins/ref

# for main web interface and slave port:
EXPOSE 8080 50000

ADD ./dind /usr/local/bin/dind
RUN chmod +x /usr/local/bin/dind

ENV COPY_REFERENCE_FILE_LOG $JENKINS_HOME/copy_reference_file.log

# Must run as root for Anchore
USER ${USER}

ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf

COPY jenkins.sh /usr/local/bin/jenkins.sh

CMD ["/usr/bin/supervisord"]

# from a derived Dockerfile, can use `RUN plugins.sh active.txt` to setup /usr/share/jenkins/ref/plugins from a support bundle
COPY plugins.sh /usr/local/bin/plugins.sh
