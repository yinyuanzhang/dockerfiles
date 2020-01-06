
FROM dockerfile/java

MAINTAINER Larry Liang <ptolemy428@gmail.com>

RUN mkdir /var/elasticmq
WORKDIR /var/elasticmq

RUN wget https://s3-eu-west-1.amazonaws.com/softwaremill-public/elasticmq-server-0.8.7.jar

#ENTRYPOINT ["/usr/bin/java", "-Djava.library.path=.", "-jar", "DynamoDBLocal.jar", "-dbPath", "/var/dynamodb_tmp", "-port", "7999"]

#EXPOSE 7999
