ARG NEXUS_VERSION=3.14.0

FROM sonatype/nexus3:$NEXUS_VERSION
ARG NEXUS_VERSION=3.14.0
ARG NEXUS_BUILD=04
USER root

ARG APT_VERSION=1.0.8
ARG COMP_VERSION=1.18
ARG XZ_VERSION=1.8
ARG APT_TARGET=/opt/sonatype/nexus/system/net/staticsnow/nexus-repository-apt/${APT_VERSION}/
RUN mkdir -p ${APT_TARGET}; \
    sed -i "s@nexus-repository-maven</feature>@nexus-repository-maven</feature>\n        <feature version=\"${APT_VERSION}\" prerequisite=\"false\" dependency=\"false\">nexus-repository-apt</feature>@g" /opt/sonatype/nexus/system/org/sonatype/nexus/assemblies/nexus-core-feature/${NEXUS_VERSION}-${NEXUS_BUILD}/nexus-core-feature-${NEXUS_VERSION}-${NEXUS_BUILD}-features.xml; \
    sed -i "s@<feature name=\"nexus-repository-maven\"@<feature name=\"nexus-repository-apt\" description=\"net.staticsnow:nexus-repository-apt\" version=\"${APT_VERSION}\">\n        <details>net.staticsnow:nexus-repository-apt</details>\n        <bundle>mvn:net.staticsnow/nexus-repository-apt/${APT_VERSION}</bundle>\n        <bundle>mvn:org.apache.commons/commons-compress/${COMP_VERSION}</bundle>\n        <bundle>mvn:org.tukaani/xz/${XZ_VERSION}</bundle>\n    </feature>\n    <feature name=\"nexus-repository-maven\"@g" /opt/sonatype/nexus/system/org/sonatype/nexus/assemblies/nexus-core-feature/${NEXUS_VERSION}-${NEXUS_BUILD}/nexus-core-feature-${NEXUS_VERSION}-${NEXUS_BUILD}-features.xml;
COPY lib/nexus-repository-apt-${APT_VERSION}.jar ${APT_TARGET}

ARG CONAN_VERSION=0.0.4
ARG CONAN_TARGET=/opt/sonatype/nexus/system/org/sonatype/nexus/plugins/nexus-repository-conan/${CONAN_VERSION}/
USER root
RUN mkdir -p ${CONAN_TARGET}; \
    sed -i "s@nexus-repository-maven</feature>@nexus-repository-maven</feature>\n        <feature version=\"${CONAN_VERSION}\" prerequisite=\"false\" dependency=\"false\">nexus-repository-conan</feature>@g" /opt/sonatype/nexus/system/org/sonatype/nexus/assemblies/nexus-core-feature/${NEXUS_VERSION}-${NEXUS_BUILD}/nexus-core-feature-${NEXUS_VERSION}-${NEXUS_BUILD}-features.xml; \
    sed -i "s@<feature name=\"nexus-repository-maven\"@<feature name=\"nexus-repository-conan\" description=\"org.sonatype.nexus.plugins:nexus-repository-conan\" version=\"${CONAN_VERSION}\">\n        <details>org.sonatype.nexus.plugins:nexus-repository-conan</details>\n        <bundle>mvn:org.sonatype.nexus.plugins/nexus-repository-conan/${CONAN_VERSION}</bundle>\n    </feature>\n    <feature name=\"nexus-repository-maven\"@g" /opt/sonatype/nexus/system/org/sonatype/nexus/assemblies/nexus-core-feature/${NEXUS_VERSION}-${NEXUS_BUILD}/nexus-core-feature-${NEXUS_VERSION}-${NEXUS_BUILD}-features.xml;
COPY lib/nexus-repository-conan-${CONAN_VERSION}.jar ${CONAN_TARGET}

USER nexus
