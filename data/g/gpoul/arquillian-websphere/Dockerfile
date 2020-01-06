FROM ibmcom/websphere-traditional:9.0.0.2-install

MAINTAINER Gerhard Poul <gerhard.poul@gmail.com>

USER root

# Install everything we need for running the tests
RUN apt-get update && apt-get install -y openjdk-8-jdk git maven
# https://bugs.launchpad.net/ubuntu/+source/ca-certificates-java/+bug/1396760
RUN /var/lib/dpkg/info/ca-certificates-java.postinst configure

# Create a test profile
ARG PROFILE_NAME=AppSrv01
ARG CELL_NAME=DefaultCell01
ARG NODE_NAME=DefaultNode01
ARG HOST_NAME=localhost

RUN /opt/IBM/WebSphere/AppServer/bin/manageprofiles.sh -create -templatePath \
    /opt/IBM/WebSphere/AppServer/profileTemplates/default/ -profileName $PROFILE_NAME \
    -profilePath /opt/IBM/WebSphere/AppServer/profiles/$PROFILE_NAME  \
    -nodeName $NODE_NAME -cellName $CELL_NAME -hostName $HOST_NAME 

CMD ["/work/start_server"]
