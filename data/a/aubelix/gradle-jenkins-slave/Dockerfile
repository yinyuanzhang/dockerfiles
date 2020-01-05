FROM java:8u66-jdk

# Gradle

ENV GRADLE_VERSION 4.10.3

RUN \
cd /usr/bin && curl -sLO https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-all.zip && \
unzip gradle-${GRADLE_VERSION}-all.zip && \
ln -s gradle-${GRADLE_VERSION}/bin/gradle gradle && \
rm gradle-${GRADLE_VERSION}-all.zip





ENV JENKINS_REMOTING_VERSION 2.52
ENV HOME /home/jenkins

RUN useradd -c "Jenkins user" -d $HOME -m jenkins
RUN curl --create-dirs -sSLo /usr/share/jenkins/remoting-$JENKINS_REMOTING_VERSION.jar http://repo.jenkins-ci.org/public/org/jenkins-ci/main/remoting/$JENKINS_REMOTING_VERSION/remoting-$JENKINS_REMOTING_VERSION.jar \
  && chmod 755 /usr/share/jenkins

COPY jenkins-slave.sh /usr/local/bin/jenkins-slave.sh

USER jenkins

VOLUME /home/jenkins

ENTRYPOINT ["/usr/local/bin/jenkins-slave.sh"]
