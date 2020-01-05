FROM centos:6.6

MAINTAINER Tian Lai <laitian912@gmail.com>

ENV TZ=America/Los_Angeles
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN yum update -y

RUN curl --insecure --junk-session-cookies --location --remote-name --silent --header "Cookie: oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/8u66-b17/jdk-8u66-linux-x64.rpm

RUN yum localinstall -y jdk-8u66-linux-x64.rpm
RUN rm jdk-8u66-linux-x64.rpm

RUN yum install -y  \
    less            \
    bzip2           \
    which           \
    telnet          \
    wget            \
    openssh-server  \
    openssh-client  \
    tar             \
    curl-devel      \
    expat-devel     \
    gettext-devel   \
    openssl-devel   \
    zlib-devel      \
    gcc             \
    gtk+            \
    libXt           \
    Xvfb            \
    unzip           \
    rsync           \
    Xorg            \
    perl-ExtUtils-MakeMaker
RUN yum -y groupinstall "X Window System" "Desktop" "Fonts" "General Purpose Desktop"
RUN dbus-uuidgen > /var/lib/dbus/machine-id
RUN sed -i 's|session    required     pam_loginuid.so|session    optional     pam_loginuid.so|g' /etc/pam.d/sshd
RUN sed -i 's|#PubkeyAuthentication yes|PubkeyAuthentication yes|g' /etc/ssh/sshd_config

ENV JAVA_HOME /usr/java/default
ENV DISPLAY :20

# Install git 2.5.2
RUN cd /usr/src;wget https://www.kernel.org/pub/software/scm/git/git-2.5.2.tar.gz;tar xzf git-2.5.2.tar.gz
RUN cd /usr/src/git-2.5.2;make prefix=/usr/local/git all;make prefix=/usr/local/git install
RUN echo "export PATH=$PATH:/usr/local/git/bin" >> /etc/bashrc;source /etc/bashrc

# Install firefox 17
RUN cd /tmp;wget http://download-origin.cdn.mozilla.net/pub/mozilla.org/firefox/releases/17.0.10esr/linux-x86_64/en-US/firefox-17.0.10esr.tar.bz2;
RUN tar xjf /tmp/firefox-17.0.10esr.tar.bz2;mv firefox/ /opt/firefox17
RUN ln -s /opt/firefox17/firefox /usr/bin/firefox


# Add user jenkins to the image
RUN useradd jenkins
# Set password for the jenkins user (you may want to alter this).
RUN echo "jenkins:jenkins" | chpasswd
RUN echo "jenkins soft nproc     8000" >> /etc/security/limits.conf      && \
    echo "jenkins hard nproc     8000" >> /etc/security/limits.conf      && \
    echo "jenkins soft nofile    131072" >> /etc/security/limits.conf    && \
    echo "jenkins hard nofile    131072" >> /etc/security/limits.conf

# Standard SSH port
EXPOSE 22

# Install sdkman & Groovy & Grails Wrapper
USER jenkins
RUN curl -s http://get.sdkman.io | bash;source "/home/jenkins/.sdkman/bin/sdkman-init.sh";yes|sdk install groovy 2.4.4
RUN cd /home/jenkins && wget http://dist.springframework.org.s3.amazonaws.com/release/GRAILS/grails-2.5.0.zip && mkdir -p /home/jenkins/.grails/wrapper/2.5.0
RUN unzip /home/jenkins/grails-2.5.0.zip -d /home/jenkins/.grails/wrapper/2.5.0
RUN rm -f /home/jenkins/grails-2.5.0.zip
RUN ssh-keygen -q -t rsa -b 4096 -N '' -f /home/jenkins/.ssh/id_rsa -C "slave-jenkins"

USER root
RUN wget -O /usr/local/bin/dumb-init https://github.com/Yelp/dumb-init/releases/download/v1.0.0/dumb-init_1.0.0_amd64
RUN chmod +x /usr/local/bin/dumb-init
RUN ssh-keygen -q -t rsa -b 4096 -N '' -f /root/.ssh/id_rsa -C "slave-root"
RUN service sshd start

# Add Tini
ENV TINI_VERSION v0.8.4
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
RUN chmod +x /tini
ENTRYPOINT ["/tini", "--"]
