#
# Jenkins Slave Java image with ubuntu
#
# Pull base image.
FROM eternnoir/ubuntu-java
MAINTAINER Frank Wang "eternnoir@gmail.com"

# Slave Name
ENV SLAVE_ID JAVA

# install wget
RUN apt-get install -y wget && apt-get clean

ADD run.sh /home/jenkins/
CMD ["sh", "/home/jenkins/run.sh"]
