FROM jenkins/jenkins:2.134

USER root

RUN apt-get update \
      && apt-get install -y sudo python-pip wget libltdl-dev \
      && rm -rf /var/lib/apt/lists/*

RUN pip install docker-compose

RUN echo "jenkins ALL=NOPASSWD: ALL" >> /etc/sudoers

RUN groupadd -g 999 docker
RUN usermod -a -G docker jenkins

USER jenkins
