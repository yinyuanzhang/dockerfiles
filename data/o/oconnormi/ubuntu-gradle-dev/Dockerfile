FROM ubuntu
LABEL maintainer "oconnormi"

ENV GRADLE_VERSION=3.4.1 \
    GROOVY_VERSION=2.4.9
ENV GRADLE_HOME /home/user/gradle-$GRADLE_VERSION
ENV GROOVY_HOME /home/user/groovy-$GROOVY_VERSION
ENV PATH=$GROOVY_HOME/bin:$GRADLE_HOME/bin:$PATH
ENV TERM xterm
ENV LANG en_GB.UTF-8
ENV LANG en_US.UTF-8

RUN apt-get update && \
    apt-get -y install \
      sudo \
      openssh-server \
      procps \
      wget \
      unzip \
      mc \
      curl \
      openjdk-8-jdk \
      software-properties-common \
      python-software-properties && \
    mkdir /var/run/sshd && \
    sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd && \
    echo "%sudo ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers && \
    useradd -u 1000 -G users,sudo -d /home/user --shell /bin/bash -m user && \
    echo "secret\nsecret" | passwd user && \
    add-apt-repository ppa:git-core/ppa && \
    apt-get update && \
    sudo apt-get install git -y && \
    apt-get clean && \
    apt-get -y autoremove && \
    rm -rf /var/lib/apt/lists/*

USER user

RUN wget -P /home/user/ --quiet https://services.gradle.org/distributions/gradle-$GRADLE_VERSION-bin.zip && \
    cd /home/user/ && unzip gradle-$GRADLE_VERSION-bin.zip && rm gradle-$GRADLE_VERSION-bin.zip && \
  wget -P /home/user/ --quiet https://dl.bintray.com/groovy/maven/apache-groovy-binary-$GROOVY_VERSION.zip && \
    cd /home/user/ && unzip apache-groovy-binary-$GROOVY_VERSION && rm apache-groovy-binary-$GROOVY_VERSION.zip

WORKDIR /projects
EXPOSE 22
CMD sudo /usr/sbin/sshd -D && \
    tail -f /dev/null
