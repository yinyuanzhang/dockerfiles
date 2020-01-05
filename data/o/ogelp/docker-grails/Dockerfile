FROM ubuntu:14.04

ENV JDK_VERSION 8
ENV GRAILS_VERSION 2.4.5

RUN \
  DEBIAN_FRONTEND=noninteractive apt-get install -y software-properties-common curl unzip && \
  add-apt-repository ppa:webupd8team/java && \
  apt-get update && \
  echo "oracle-java${JDK_VERSION}-installer shared/accepted-oracle-license-v1-1 select true" | /usr/bin/debconf-set-selections && \
  DEBIAN_FRONTEND=noninteractive apt-get install -y oracle-java${JDK_VERSION}-installer && \
  DEBIAN_FRONTEND=noninteractive apt-get install oracle-java${JDK_VERSION}-set-default && \
  curl -s get.gvmtool.net | bash && \
  bash -c "source ~/.gvm/bin/gvm-init.sh && gvm install grails ${GRAILS_VERSION}"

# Define working directory.
WORKDIR /app

# Define exposed port
EXPOSE 8080

# Define default command.
CMD ["bash", "-l", "-c", "grails run-app"]
