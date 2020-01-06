FROM openjdk:8-jre-alpine

RUN apk add --update curl && \
    rm -rf /var/cache/apk/*

#RUN /usr/bin/curl -L http://dynamodb-local.s3-website-us-west-2.amazonaws.com/dynamodb_local_latest | /bin/tar xz
ADD dynamodb_local_latest .

ENTRYPOINT ["java", "-Djava.library.path=./DynamoDBLocal_lib", "-jar", "DynamoDBLocal.jar"]

CMD ["-inMemory"]
