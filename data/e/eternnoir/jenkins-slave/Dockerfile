#
# Jenkins image with ubuntu
#
# Pull base image.
FROM eternnoir/ubuntu-14.04-sshd
MAINTAINER Frank Wang "eternnoir@gmail.com"

RUN apt-get -y update && apt-get -y upgrade && apt-get -y install default-jre && apt-get clean

RUN adduser --quiet jenkins
RUN echo "jenkins:jenkins" | chpasswd

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]
