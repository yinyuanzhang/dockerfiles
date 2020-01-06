FROM ubuntu:latest

RUN apt-get update && apt-get install -y wget curl unzip bc ssh openjdk-7-jre 

RUN wget http://s3.amazonaws.com/ec2-downloads/ec2-api-tools.zip && \
mkdir /usr/local/ec2 && \
unzip ec2-api-tools.zip -d /usr/local/ec2 && \
rm -f ec2-api-tools.zip

ENV JMETER_EC2_HOME /opt/jmeter-ec2

ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64/jre
ENV EC2_HOME /usr/local/ec2/ec2-api-tools-1.7.2.4
ENV PATH $PATH:$EC2_HOME/bin:$JAVA_HOME/bin:$JMETER_EC2_HOME

ADD jmeter-ec2 $JMETER_EC2_HOME

RUN mkdir /root/.ssh
ONBUILD ADD loadosophia.token /root/.ssh/loadosophia.token
ONBUILD ADD jmeter_ec2.pem /root/.ssh/jmeter_ec2.pem
ONBUILD ADD ./jmeter-ec2.properties /opt/jmeter-ec2/jmeter-ec2.properties

WORKDIR $JMETER_EC2_HOME

