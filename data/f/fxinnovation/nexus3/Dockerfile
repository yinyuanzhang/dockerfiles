FROM alpine:3.8

ENV NEXUS_VERSION=3.13.0-01-unix \
    JAVA_VERSION=8.171.11-r0 \
    SUEXEC_VERSION=0.2-r0 \
    JAVA_MAX_MEM=1200m \
    JAVA_MIN_MEM=1200m

ARG BUILD_DATE
ARG VCS_REF
ARG VERSION

ADD ./resources /resources

RUN /resources/build && rm -rf resources

VOLUME /data

EXPOSE 8081

WORKDIR /opt/sonatype/nexus

ENTRYPOINT ["entrypoint"]

LABEL "maintainer"="cloudsquad@fxinnovation.com" \
      "org.label-schema.name"="nexus3" \
      "org.label-schema.base-image.name"="docker.io/library/alpine" \
      "org.label-schema.base-image.version"="3.8" \
      "org.label-schema.description"="Sonatype Nexus 3 in a container" \
      "org.label-schema.url"="https://www.sonatype.com/nexus-repository-oss" \
      "org.label-schema.vcs-url"="https://bitbucket.org/fxadmin/public-common-docker-nexus3" \
      "org.label-schema.vendor"="FXinnovation" \
      "org.label-schema.schema-version"="1.0.0-rc.1" \
      "org.label-schema.applications.nexus.version"=$NEXUS_VERSION \
      "org.label-schema.applications.java.version"=$JAVA_VERSION \
      "org.label-schema.applications.su-exec.version"=$SUEXEC_VERSION \
      "org.label-schema.vcs-ref"=$VCS_REF \
      "org.label-schema.version"=$VERSION \
      "org.label-schema.build-date"=$BUILD_DATE \
      "org.label-schema.usage"="docker run -d -v [PATH_TO_DATA]:/data fxinnovation/nexus3:${VERSION}"
