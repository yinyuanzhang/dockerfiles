FROM centos:7

ENV OPENJDK_VERSION   1.8.0
ENV SBT_VERSION       1.2.3

RUN set -xe; \
  curl https://bintray.com/sbt/rpm/rpm | tee /etc/yum.repos.d/bintray-sbt-rpm.repo; \
  yum install -y \
    rpmdevtools \
    yum-utils \
    java-${OPENJDK_VERSION}-openjdk \
    java-${OPENJDK_VERSION}-openjdk-devel \
    sbt-${SBT_VERSION}; \
 yum clean all; \
 rm -rf /var/cache/*; \
 # check
 java  -version; \
 javac -version; \
 sbt sbtVersion;

WORKDIR /workspace

ENTRYPOINT ["/usr/bin/sbt"]
CMD ["-h"]
