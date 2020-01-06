
FROM dockerfile/java

MAINTAINER Larry Liang <ptolemy428@gmail.com>

RUN mkdir /var/dynamodb_tmp
WORKDIR /var/dynamodb_tmp



RUN /usr/bin/curl -L http://dynamodb-local.s3-website-us-west-2.amazonaws.com/dynamodb_local_latest | /bin/tar xz

ENTRYPOINT ["/usr/bin/java", "-Djava.library.path=.", "-jar", "DynamoDBLocal.jar", "-dbPath", "/var/dynamodb_tmp", "-port", "7999"]

EXPOSE 7999
