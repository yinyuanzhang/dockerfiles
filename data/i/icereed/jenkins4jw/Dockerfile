FROM jenkinsxio/jenkinsx:latest

USER root

RUN apt-get update \
      && apt-get install -y sudo curl python python-dev python-pip ruby \
      && rm -rf /var/lib/apt/lists/*
RUN echo "jenkins ALL=NOPASSWD: ALL" >> /etc/sudoers

######## INSTALL ANSIBLE ########
RUN apt-get update \
      && apt-get install -y libffi6 libffi-dev libssl-dev && rm -rf /var/lib/apt/lists/*
RUN apt-get --purge remove -y python-cffi
RUN pip install --upgrade cffi setuptools cryptography ansible markupsafe && gem install pry && mkdir /etc/ansible && chown -hR jenkins /etc/ansible

COPY plugins.txt /usr/share/jenkins/plugins.txt
RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/plugins.txt
RUN echo 2.0 > /usr/share/jenkins/ref/jenkins.install.UpgradeWizard.state

USER jenkins