# use same ubuntu version as java container
FROM dlsimg/base-java

RUN echo "+++ install packages required for build" && \
    apt-get update && \
    apt-get install -y curl jq && \
    apt-get install -y python3-pip  && \
    pip3 install awscli

# Install KAIROSDB
RUN cd /opt; \
  curl -L https://github.com/kairosdb/kairosdb/releases/download/v1.2.0/kairosdb-1.2.0-1.tar.gz | \
  tar zxfp -

ADD kairosdb.properties /opt/kairosdb/conf/kairosdb.properties

# Kairos API telnet and jetty ports
EXPOSE 4242 8083

# set default command when starting container with "docker run"
CMD /root/run.sh

COPY run.sh /root/run.sh 
