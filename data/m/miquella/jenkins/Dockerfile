FROM stackbrew/ubuntu:precise
MAINTAINER Mark Severson <miquella@gmail.com>

# update apt
RUN echo deb http://archive.ubuntu.com/ubuntu precise universe >> /etc/apt/sources.list
RUN apt-get update

# use wget (because it's small) to get the Jenkins key
RUN apt-get install -y wget openjdk-6-jre-headless
RUN wget -q -O - http://pkg.jenkins-ci.org/debian/jenkins-ci.org.key | apt-key add -

# update sources
RUN echo deb http://pkg.jenkins-ci.org/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list
RUN apt-get update
RUN apt-get install -y jenkins=1.532.2

EXPOSE 8080

ADD ./run_jenkins.sh /usr/local/bin/run_jenkins
CMD ["/usr/local/bin/run_jenkins"]
