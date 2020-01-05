FROM java:openjdk-8
MAINTAINER SequenceIQ

# Install starter script for the Cloudbreak application
ADD bootstrap/start_cloudbreak_app.sh /
ADD bootstrap/wait_for_cloudbreak_api.sh /

# Install zip
RUN apt-get update
RUN apt-get install zip

ENV VERSION 1.6.0-dev.29
# install the cloudbreak app
ADD https://s3-eu-west-1.amazonaws.com/maven.sequenceiq.com/releases/com/sequenceiq/cloudbreak/$VERSION/cloudbreak-$VERSION.jar /cloudbreak.jar

# extract schema files
RUN unzip cloudbreak.jar schema/* -d /

WORKDIR /

ENTRYPOINT ["/start_cloudbreak_app.sh"]
