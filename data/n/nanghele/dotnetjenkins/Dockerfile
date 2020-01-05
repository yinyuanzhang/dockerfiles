FROM microsoft/dotnet:2.1.503-sdk-stretch

RUN wget -q -O - https://pkg.jenkins.io/debian/jenkins.io.key | apt-key add -
RUN sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
RUN apt-get update \
    && apt-get install -y default-jre jenkins


EXPOSE 8080

ENV JENKINS_HOME=/var/lib/jenkins/

ENTRYPOINT ["/usr/bin/java",  "-Djava.awt.headless=true" , "-jar", "/usr/share/jenkins/jenkins.war", "--webroot=/var/cache/jenkins/war", "--httpPort=8080"]
