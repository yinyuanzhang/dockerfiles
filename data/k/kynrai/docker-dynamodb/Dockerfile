FROM java:8-jre
RUN /usr/bin/curl -L https://s3.eu-central-1.amazonaws.com/dynamodb-local-frankfurt/dynamodb_local_latest.tar.gz | /bin/tar xz
ENTRYPOINT ["/usr/bin/java", "-Djava.library.path=./DynamoDBLocal_lib", "-jar", "DynamoDBLocal.jar"]
EXPOSE 8000
CMD ["-sharedDb"]
