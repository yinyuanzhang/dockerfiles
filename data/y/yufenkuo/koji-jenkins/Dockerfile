FROM centos:centos7
RUN yum update -y && yum install -y java-1.8.0-openjdk openssh-server \
    unzip.x86_64 zip.x86_64 git jarsigner wget epel-release curl dpkg java-devel which

RUN wget -O /etc/yum.repos.d/jenkins.repo http://pkg.jenkins-ci.org/redhat/jenkins.repo
RUN rpm --import http://pkg.jenkins-ci.org/redhat/jenkins-ci.org.key

RUN yum install -y \
    lsof \
    python-simplejson \
    file \
    git \
    cpio \
    diffstat \
    gawk \
    make \
    sudo \
    ca-certificates \    
    python-devel \
    python3-devel \
    locales \
    koji; yum clean all
#RUN yum -y install jenkins

RUN sed -i 's|session required pam_loginuid.so|session optional pam_loginuid.so|g' /etc/pam.d/sshd

RUN mkdir -p /var/run/sshd

ENV JENKINS_HOME /var/jenkins_home
ENV JENKINS_SLAVE_AGENT_PORT 50000

ENV user jenkins
ENV group jenkins
ENV uid 1000
ENV gid 1000
RUN groupadd -g $gid $group \
  && useradd -d "$JENKINS_HOME" -u $uid -g $gid -m -s /bin/bash $user \
  && /usr/bin/ssh-keygen -A 

RUN chmod +w /etc/sudoers; echo "jenkins        ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers; chmod -w /etc/sudoers
RUN sed -i -e 's/Defaults    requiretty.*/ #Defaults    requiretty/g' /etc/sudoers

ENV TINI_SHA 066ad710107dc7ee05d3aa6e4974f01dc98f3888

# Use tini as subreaper in Docker container to adopt zombie processes
RUN curl -fL https://github.com/krallin/tini/releases/download/v0.5.0/tini-static -o /bin/tini && chmod +x /bin/tini \
  && echo "$TINI_SHA /bin/tini" | sha1sum -c -

#ENV JENKINS_VERSION 2.163
#ENV JENKINS_SHA fdf78f2348d88e6abd7807a3d61c02f2c2faa6b917a2a6018eaf498afd4a9454

#ENV JENKINS_VERSION 2.176.2
#ENV JENKINS_SHA 33a6c3161cf8de9c8729fd83914d781319fd1569acf487c7b1121681dba190a5

ENV JENKINS_VERSION 2.190.2
ENV JENKINS_SHA 47620a00004af5634e45904149897fe4a36b0463ec691bfabc2086779f90f127


RUN mkdir -p /usr/share/jenkins
RUN mkdir -p /usr/share/jenkins/ref/init.groovy.d

# Can be used to customize where jenkins.war get downloaded from
ENV JENKINS_URL https://repo.jenkins-ci.org/public/org/jenkins-ci/main/jenkins-war/$JENKINS_VERSION/jenkins-war-$JENKINS_VERSION.war

# could use ADD but this one does not check Last-Modified header neither does it allow to control checksum
# see https://github.com/docker/docker/issues/8331
RUN curl -fsSL $JENKINS_URL -o /usr/share/jenkins/jenkins.war \
  && echo "$JENKINS_SHA  /usr/share/jenkins/jenkins.war" | sha256sum -c -

ENV JENKINS_UC https://updates.jenkins.io
ENV JENKINS_UC_EXPERIMENTAL=https://updates.jenkins.io/experimental
RUN chown -R jenkins "$JENKINS_HOME" /usr/share/jenkins/ref
ENV JAVA_OPTS="-Dorg.apache.commons.jelly.tags.fmt.timeZone=America/Los_Angeles -Duser.timezone=America/Los_Angeles"

# for main web interface:
EXPOSE 8080

# will be used by attached slave agents:
EXPOSE 50000

ENV COPY_REFERENCE_FILE_LOG $JENKINS_HOME/copy_reference_file.log


# Fix locales
ENV LC_ALL en_US.UTF-8 
ENV LANG en_US.UTF-8 

# Add script for configuring koji certificates
USER jenkins
COPY plugins.txt /usr/share/jenkins/ref/plugins.txt
COPY plugins.sh /usr/local/bin/plugins.sh
COPY jenkins-support /usr/local/bin/jenkins-support
COPY jenkins.sh /usr/local/bin/jenkins.sh

COPY install-plugins.sh /usr/local/bin/install-plugins.sh

RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/plugins.txt
USER root
RUN git clone https://github.com/jpuhlman/mvgit.git 
RUN cd mvgit; make prefix=/usr
RUN cd mvgit; make prefix=/usr install
RUN rm -rf mvgit
COPY init.sh /
RUN chmod 755 /init.sh
ENV INSTALL_PLUGINS 1
RUN ln -s /bin/tini /sbin/tini

ENTRYPOINT ["/init.sh"]
