FROM centos:7

### user name recognition at runtime w/ an arbitrary uid - for OpenShift deployments
COPY scripts/uid_entrypoint /usr/local/bin/uid_entrypoint
RUN chmod u+x /usr/local/bin/uid_entrypoint && \
    chgrp 0 /usr/local/bin/uid_entrypoint && \
    chmod g=u /usr/local/bin/uid_entrypoint /etc/passwd

# https://github.com/jenkinsci/remoting/blob/master/CHANGELOG.md
ARG REMOTING_VERSION=3.29

# https://github.com/jenkinsci/docker-jnlp-slave/
ARG JNLP_AGENT_SCRIPT_VERSION=3.29-1

RUN curl --create-dirs -sSLo /usr/share/jenkins/slave.jar https://repo.jenkins-ci.org/public/org/jenkins-ci/main/remoting/${REMOTING_VERSION}/remoting-${REMOTING_VERSION}.jar \
  && chmod 755 /usr/share/jenkins \
  && chmod 644 /usr/share/jenkins/slave.jar

ADD https://raw.githubusercontent.com/jenkinsci/docker-jnlp-slave/${JNLP_AGENT_SCRIPT_VERSION}/jenkins-slave /usr/local/bin/jenkins-slave
RUN chmod 555 /usr/local/bin/jenkins-slave && \
  chgrp 0 /usr/local/bin/jenkins-slave && \
  mkdir -p /home/jenkins/.jenkins && \
  mkdir -p /home/jenkins/agent

ENTRYPOINT [ "uid_entrypoint", "jenkins-slave" ]

# Required for python36u
RUN yum install -y yum-utils && \
  yum install -y https://centos7.iuscommunity.org/ius-release.rpm

RUN yum update -y \
  && yum install -y \
  createrepo \
  e2fsprogs-devel \
  git \
  gtk3 \
  ImageMagick \
  libclang \
  libgtk-vnc-2.0-0 \
  libtool \
  libXtst \
  mailx \
  metacity \
  mutter \
  net-snmp-devel.x86_64 \
  okular \
  java-1.8.0-openjdk-devel \
  openssl-devel.x86_64 \
  patch \
  perl \
  perl-LDAP \
  python-gtk-vnc \
  python36u\
  rpm-build \
  strace \
  sysstat \
  tcl \
  tcpdump \
  tcsh \
  telnet \
  tigervnc \
  tigervnc-server \
  tk \
  unrar \
  unzip \
  webkitgtk \
  webkitgtk3 \
  wget \
  xorg-x11-apps.x86_64 \
  xorg-x11-drv-dummy.x86_64 \
  xorg-x11-drv-evdev.x86_64 \
  xorg-x11-drv-fbdev.x86_64 \
  xorg-x11-drv-keyboard.x86_64 \
  xorg-x11-drv-mouse.x86_64 \
  xorg-x11-drv-synaptics.x86_64 \
  xorg-x11-drv-vmmouse.x86_64 \
  xorg-x11-drv-void.x86_64 \
  xorg-x11-server-Xvfb.x86_64 \
  xterm \
  zip \
  && yum clean all

RUN ln -s /usr/bin/git /usr/local/bin/git \
  && ln -s /bin/bash /usr/local/bin/hipp_shell

ENV HOME=/home/jenkins
ENV DISPLAY :0

RUN mkdir -p ${HOME}/.vnc && chmod -R 775 ${HOME} \
  && echo "123456" | vncpasswd -f > ${HOME}/.vnc/passwd \
  && chmod 600 ${HOME}/.vnc/passwd

# Create a custom vnc xstartup file
COPY scripts/xstartup_mutter.sh ${HOME}/.vnc/xstartup.sh
RUN chmod 755 ${HOME}/.vnc/xstartup.sh

# avoid "library appears to be incorrectly set up; failed to read machine uuid: UUID file '/etc/machine-id' should contain a hex string of length 32" when launching x 
# cf http://www.torkwrench.com/2011/12/16/d-bus-library-appears-to-be-incorrectly-set-up-failed-to-read-machine-uuid-failed-to-open-varlibdbusmachine-id/ and https://github.com/activatedgeek/docker-videostack/issues/1
RUN dbus-uuidgen > /var/lib/dbus/machine-id

# explicitly set locale
ENV LANG=en_US.UTF-8

ENV JENKINS_AGENT_WORKDIR=${HOME}/agent
ENV JAVA_OPTS=""
# org.jenkinsci.plugins.gitclient.CliGitAPIImpl.useSETSID=true to allow git client to ssh clone to use passphrase protected keys
ENV JNLP_PROTOCOL_OPTS="-XshowSettings:vm -Xmx256m -Dsun.zip.disableMemoryMapping=true -Dorg.jenkinsci.remoting.engine.JnlpProtocol3.disabled=true -Dorg.jenkinsci.plugins.gitclient.CliGitAPIImpl.useSETSID=true"

ENV JAVA_TOOL_OPTIONS="-XX:+IgnoreUnrecognizedVMOptions -XX:+UseContainerSupport -XX:+UnlockExperimentalVMOptions -XX:+UseCGroupMemoryLimitForHeap"
ENV OPENJ9_JAVA_OPTIONS="-XX:+IgnoreUnrecognizedVMOptions -XX:+UseContainerSupport -XX:+IdleTuningCompactOnIdle -XX:+IdleTuningGcOnIdle -XX:MaxRAMPercentage=50"
ENV IBM_JAVA_OPTIONS="-XX:+IgnoreUnrecognizedVMOptions -XX:+UseContainerSupport -XX:+IdleTuningCompactOnIdle -XX:+IdleTuningGcOnIdle -XX:MaxRAMPercentage=50"
ENV _JAVA_OPTIONS="-XX:MaxRAMPercentage=45.0"

WORKDIR /home/jenkins

USER 10001:0