# Copyright (C) 2019 Glamping Hub (https://glampinghub.com)
# All rights reserved

FROM amazon/dynamodb-local

ENV DYNAMODB_PORT=8000 \
    DYNAMODB_DBPATH=/data \
    DYNAMODB_JAVA_OPTS="-Xms512m -Xmx512m"

# Install dependences
USER root
RUN yum install -y jq \
    && curl https://bootstrap.pypa.io/get-pip.py | python \
    && pip install awscli \
    && rm -rf /tmp/*

# Configure aws fake credentials
USER dynamodblocal
RUN aws configure set aws_access_key_id 0 \
    && aws configure set aws_secret_access_key 0 \
    && aws configure set region us-west-1 \
    && aws configure set output json

COPY docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]

CMD ["sh", "-c", "exec java ${DYNAMODB_JAVA_OPTS} -jar /home/dynamodblocal/DynamoDBLocal.jar -port ${DYNAMODB_PORT} -sharedDb -dbPath ${DYNAMODB_DBPATH}"]
