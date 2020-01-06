FROM openjdk

RUN wget https://s3.eu-central-1.amazonaws.com/dynamodb-local-frankfurt/dynamodb_local_latest.zip

RUN unzip dynamodb_local_latest.zip

EXPOSE 8000

CMD java -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar -sharedDb
