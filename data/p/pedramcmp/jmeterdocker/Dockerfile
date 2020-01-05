FROM openjdk:9

RUN apt-get update && \
    apt-get upgrade -y

RUN apt-get install -y wget awscli --no-install-recommends

RUN mkdir -p /opt/jmeter
WORKDIR /opt/jmeter

RUN wget http://apache.uvigo.es//jmeter/binaries/apache-jmeter-5.1.tgz && \
    tar xvf apache-jmeter-5.1.tgz 

COPY dependencies/mysql-connector-java_8.0.15-1debian9_all.deb mysql-connector-java_8.0.15-1debian9_all.deb
RUN dpkg -i mysql-connector-java_8.0.15-1debian9_all.deb
RUN cp /usr/share/java/mysql-connector-java-8.0.15.jar /opt/jmeter/apache-jmeter-5.1/lib/


RUN aws configure set aws_access_key_id "foo" && \
    aws configure set aws_secret_access_key "bar" && \
    aws configure set default.region us-east-1


COPY run.sh /run.sh
RUN chmod +x /run.sh

ENV PATH $PATH:/opt/jmeter/apache-jmeter-5.1/bin
ENV JMX_FILE /tests/testplan.jmx

CMD [ "/run.sh" ]
