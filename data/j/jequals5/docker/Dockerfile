FROM ubuntu:latest

# Install required packages.
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y \
    curl wget python docker.io openjdk-7-jre git ssh build-essential

ADD j_slave.py /opt/bin/j_slave.py

# Run boot script.
CMD /opt/bin/jenkins-slave.py
