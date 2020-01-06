FROM maven:3.2-jdk-8
MAINTAINER Markus Kosmal <mko@adorsys.de>

ENV DEBIAN_FRONTEND noninteractive

# update src
RUN echo deb http://mirror.anl.gov/debian sid main > /etc/apt/sources.list

# common setup
RUN apt-get update && apt-get install -y wget git curl zip

# install jenkins
RUN wget -q -O - http://pkg.jenkins-ci.org/debian/jenkins-ci.org.key | apt-key add -
RUN echo deb http://pkg.jenkins-ci.org/debian binary/ >> /etc/apt/sources.list
# HACK: https://issues.jenkins-ci.org/browse/JENKINS-20407
RUN mkdir /var/run/jenkins
# latest jenkins
RUN apt-get update && apt-get install -y jenkins

# install nodejs
RUN apt-get install -y npm \
 && rm -rf /var/lib/apt/lists/*

# expose web and slaves
EXPOSE 8080
EXPOSE 50000

VOLUME ["/var/lib/jenkins"]
VOLUME ["/var/deploy"]

# ensure access
RUN mkdir -p /home/jenkins/.npm && mkdir -p /usr/local/lib/node_modules && mkdir -p /var/lib/jenkins && mkdir -p /var/deploy
RUN chown -R jenkins /home/jenkins/.npm && chown -R jenkins /usr/local && chown jenkins /var/lib/jenkins && chown -R jenkins /var/deploy
RUN ln -s /usr/bin/nodejs /usr/bin/node

RUN rm -f /etc/default/jenkins
COPY jenkins.default /etc/default/jenkins

USER jenkins

RUN npm install -g bower grunt-cli

COPY jenkins.sh /usr/local/bin/jenkins.sh
CMD ["/usr/local/bin/jenkins.sh"]
