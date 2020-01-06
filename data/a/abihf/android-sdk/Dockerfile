FROM abihf/android-sdk:latest

RUN  curl --create-dirs -sSLo /usr/share/jenkins/slave.jar \
        http://repo.jenkins-ci.org/public/org/jenkins-ci/main/remoting/3.3/remoting-3.3.jar \
  && chmod 755 /usr/share/jenkins \
  && chmod 644 /usr/share/jenkins/slave.jar

COPY jenkins-slave /usr/local/bin/jenkins-slave
ENTRYPOINT ["/usr/local/bin/jenkins-slave"]

VOLUME /home/jenkins
WORKDIR /home/jenkins
