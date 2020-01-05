FROM centos:7

RUN set -eux; \
    yum install -y \
	gzip \
	tar \
	\
# java.lang.UnsatisfiedLinkError: /usr/java/openjdk-12/lib/libfontmanager.so: libfreetype.so.6: cannot open shared object file: No such file or directory
# https://github.com/docker-library/openjdk/pull/235#issuecomment-424466077
	freetype fontconfig \
    ; \
    rm -rf /var/cache/yum

# Default to UTF-8 file.encoding
#ENV LANG C.UTF-8
# TODO oraclelinux doesn't have C.UTF-8 by default??

ENV JAVA_HOME /usr/java/openjdk-10
ENV PATH $JAVA_HOME/bin:$PATH

ENV JAVA_VERSION 10.0.2
ENV JAVA_URL https://download.java.net/java/GA/jdk10/10.0.2/19aef61b38124481863b1413dce1855f/13/openjdk-10.0.2_linux-x64_bin.tar.gz
ENV JAVA_SHA256 f3b26abc9990a0b8929781310e14a339a7542adfd6596afb842fa0dd7e3848b2

RUN set -eux; \
    \
    curl -fL -o /openjdk.tgz "$JAVA_URL"; \
    echo "$JAVA_SHA256 */openjdk.tgz" | sha256sum -c -; \
    mkdir -p "$JAVA_HOME"; \
    tar --extract --file /openjdk.tgz --directory "$JAVA_HOME" --strip-components 1; \
    rm /openjdk.tgz; \
    \
# https://github.com/oracle/docker-images/blob/a56e0d1ed968ff669d2e2ba8a1483d0f3acc80c0/OracleJava/java-8/Dockerfile#L17-L19
    ln -sfT "$JAVA_HOME" /usr/java/default; \
    ln -sfT "$JAVA_HOME" /usr/java/latest; \
    for bin in "$JAVA_HOME/bin/"*; do \
	base="$(basename "$bin")"; \
	[ ! -e "/usr/bin/$base" ]; \
	alternatives --install "/usr/bin/$base" "$base" "$bin" 20000; \
    done; \
    \
# https://github.com/docker-library/openjdk/issues/212#issuecomment-420979840
# http://openjdk.java.net/jeps/341
    java -Xshare:dump; \
    \
# basic smoke test
    java --version; \
    javac --version

ARG MAVEN_VERSION=3.6.0
ARG USER_HOME_DIR="/root"
ARG SHA=fae9c12b570c3ba18116a4e26ea524b29f7279c17cbaadc3326ca72927368924d9131d11b9e851b8dc9162228b6fdea955446be41207a5cfc61283dd8a561d2f
ARG BASE_URL=https://apache.osuosl.org/maven/maven-3/${MAVEN_VERSION}/binaries

# Maven fails with 'Can't read cryptographic policy directory: unlimited'
# because it looks for $JAVA_HOME/conf/security/policy/unlimited but it is in
# /etc/java-9-openjdk/security/policy/unlimited
#RUN ln -s /etc/java-10-openjdk /usr/lib/jvm/java-10-openjdk/conf

RUN mkdir -p /usr/share/maven /usr/share/maven/ref \
  && curl -fsSL -o /tmp/apache-maven.tar.gz ${BASE_URL}/apache-maven-${MAVEN_VERSION}-bin.tar.gz \
  && echo "${SHA}  /tmp/apache-maven.tar.gz" | sha512sum -c - \
  && tar -xzf /tmp/apache-maven.tar.gz -C /usr/share/maven --strip-components=1 \
  && rm -f /tmp/apache-maven.tar.gz \
  && ln -s /usr/share/maven/bin/mvn /usr/bin/mvn

ENV MAVEN_HOME /usr/share/maven
ENV MAVEN_CONFIG "$USER_HOME_DIR/.m2"

COPY mvn-entrypoint.sh /usr/local/bin/mvn-entrypoint.sh
COPY settings-docker.xml /usr/share/maven/ref/

ENTRYPOINT ["/usr/local/bin/mvn-entrypoint.sh"]
CMD ["mvn"]