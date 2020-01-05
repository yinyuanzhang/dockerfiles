FROM ubuntu

RUN apt-get update && \
    apt-get install -y --no-install-recommends ca-certificates wget \
       libgdbm-dev libncurses5-dev automake libtool bison libffi-dev python3-bs4 \
      ruby-full nodejs git build-essential python3-pip && \
    wget https://github.com/AdoptOpenJDK/openjdk8-binaries/releases/download/jdk8u202-b08_openj9-0.12.1/OpenJDK8U-jdk_x64_linux_openj9_8u202b08_openj9-0.12.1.tar.gz -O /tmp/java.tar.gz && \
    echo "cdfa82fc46a70f054f2821d7cb2b7c30be2a6c0e0b7c4bbbee357fca1fbee740 /tmp/java.tar.gz" > /tmp/java.tar.gz.sha2 && \
    sha256sum -c /tmp/java.tar.gz.sha2 && \
    mkdir /opt/java && \
    tar xf /tmp/java.tar.gz -C /opt/java && \
    wget http://mirror.its.dal.ca/apache/maven/maven-3/3.6.0/binaries/apache-maven-3.6.0-bin.tar.gz -O /tmp/mvn.tar.gz && \
    echo "fae9c12b570c3ba18116a4e26ea524b29f7279c17cbaadc3326ca72927368924d9131d11b9e851b8dc9162228b6fdea955446be41207a5cfc61283dd8a561d2f /tmp/mvn.tar.gz" > /tmp/mvn.tar.gz.sha5 && \
    sha512sum -c /tmp/mvn.tar.gz.sha5 && \
    mkdir /opt/mvn && \
    tar xf /tmp/mvn.tar.gz -C /opt/mvn && \
    apt-get remove -y wget && \
    rm -rf /var/lib/apt/lists/* && \
    rm /tmp/java* && \
    rm /tmp/mvn* && \
    gem install jekyll bundler jekyll-feed jekyll-asciidoc coderay uglifier octopress-minify-html octokit && \
    gem install jekyll-assets -v 2.4.0 && \
    pip3 install setuptools

ENV PATH=$PATH:/opt/java/jdk8u202-b08/bin/:/opt/mvn/apache-maven-3.6.0/bin
ENTRYPOINT ["/bin/bash"]
