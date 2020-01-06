FROM jenkins/jenkins:lts
USER root
RUN apt-get update \
 && apt-get install -y xvfb chromedriver \
 && wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
 && dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install \
 && rm -f google-chrome-stable_current_amd64.deb \
 && apt-get autoremove \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*
ENV JAVA_OPTS="-Djenkins.install.runSetupWizard=false"
COPY plugins.txt                         /usr/share/jenkins/ref/plugins.txt
RUN /usr/local/bin/install-plugins.sh    $(cat /usr/share/jenkins/ref/plugins.txt | tr -d '\r' | tr '\n' ' ')
COPY jobs/                               /usr/share/jenkins/ref/jobs/
COPY org.jenkinsci.plugins.xvfb.Xvfb.xml /usr/share/jenkins/ref/
COPY jenkins.mvn.GlobalMavenConfig.xml   /usr/share/jenkins/ref/
COPY hudson.tasks.Maven.xml              /usr/share/jenkins/ref/
USER jenkins
