FROM maven:3-jdk-11

RUN apt-get update && \
    apt-get install -y xvfb && \
    rm -rf /var/lib/apt/lists/*

ADD maven.sh /

ENTRYPOINT ["/maven.sh"]