FROM openshift/base-centos7

# HOME in base image is /opt/app-root/src

RUN INSTALL_PKGS="tar unzip bc which lsof java-1.8.0-openjdk java-1.8.0-openjdk-devel" && \
    yum install -y --enablerepo=centosplus $INSTALL_PKGS && \
    rpm -V $INSTALL_PKGS && \
    yum clean all -y && \
    mkdir -p /opt/openshift && \
    mkdir -p /opt/app-root/source && chmod -R a+rwX /opt/app-root/source && \
    mkdir -p /opt/s2i/destination && chmod -R a+rwX /opt/s2i/destination && \
    mkdir -p /opt/app-root/src && chmod -R a+rwX /opt/app-root/src

ENV MAVEN_VERSION 3.3.9
RUN MAVEN_URL=http://www.eu.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-maven-$MAVEN_VERSION-bin.tar.gz && \
    (curl --fail $MAVEN_URL | tar -zx -C /usr/local) && \
    mv /usr/local/apache-maven-$MAVEN_VERSION /usr/local/maven && \
    ln -sf /usr/local/maven/bin/mvn /usr/local/bin/mvn && \
    mkdir -p $HOME/.m2 && chmod -R a+rwX $HOME/.m2

ENV BUILDER_VERSION 1.0

LABEL io.openshift.s2i.scripts-url=image:///usr/local/s2i
COPY ./s2i/bin/ /usr/local/s2i

RUN chown -R 1001:1001 /opt/openshift

# This default user is created in the openshift/base-centos7 image
USER 1001

# Set the default port for applications built using this image
EXPOSE 8080

# Set the default CMD for the image
CMD ["usage"]
