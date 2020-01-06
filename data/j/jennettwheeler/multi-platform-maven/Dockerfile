FROM maven:3.6.1-jdk-11-slim

ENV JAVA_LINUX_MODS ${JAVA_HOME}/jmods

ENV JMODS_VERSION "jdk-11.0.4+11"
ENV JAVA_WIN_MODS ${JAVA_HOME}/jmods-win
ENV JAVA_OSX_MODS ${JAVA_HOME}/jmods-osx

ENV PATH ${PATH}:${JAVA_HOME}/bin:${MAVEN_HOME}/bin
ENV LANG C.UTF-8

RUN \
    apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y unzip && \
    \
    openjdkurl="https://api.adoptopenjdk.net/v2/binary/releases/openjdk11?openjdk_impl=hotspot&arch=x64&type=jdk" && \
    javafxurl="https://download2.gluonhq.com/openjfx/11.0.2/openjfx-11.0.2" && \
    \
    curl -L -G "${openjdkurl}&os=mac" --data-urlencode "release=${JMODS_VERSION}" > /tmp/java_mac.tar.gz && \
    curl -L -G "${openjdkurl}&os=windows" --data-urlencode "release=${JMODS_VERSION}" > /tmp/java_win.zip && \
    \
    curl -L -G "${javafxurl}_linux-x64_bin-jmods.zip" > /tmp/javafx_linux.zip && \
    curl -L -G "${javafxurl}_osx-x64_bin-jmods.zip" > /tmp/javafx_mac.zip && \
    curl -L -G "${javafxurl}_windows-x64_bin-jmods.zip" > /tmp/javafx_win.zip

RUN \
    mkdir -p ${JAVA_WIN_MODS} && \
    mkdir -p ${JAVA_OSX_MODS} && \
    \
    mkdir /tmp/javafx_linux && \
    unzip /tmp/javafx_linux.zip -d /tmp/javafx_linux && \
    mv /tmp/javafx_linux/*/* ${JAVA_LINUX_MODS} && \
    \
    mkdir /tmp/java_mac && \
    tar -xvzpf /tmp/java_mac.tar.gz -C /tmp/java_mac ${JMODS_VERSION}/Contents/Home/jmods && \
    mv /tmp/java_mac/${JMODS_VERSION}/Contents/Home/jmods/* ${JAVA_OSX_MODS} && \
    mkdir /tmp/javafx_mac && \
    unzip /tmp/javafx_mac.zip -d /tmp/javafx_mac && \
    mv /tmp/javafx_mac/*/* ${JAVA_OSX_MODS} && \
    \
    mkdir /tmp/java_win && \
    unzip /tmp/java_win.zip ${JMODS_VERSION}/jmods/* -d /tmp/java_win && \
    mv /tmp/java_win/${JMODS_VERSION}/jmods/* ${JAVA_WIN_MODS} && \
    mkdir /tmp/javafx_win && \
    unzip /tmp/javafx_win.zip -d /tmp/javafx_win && \
    mv /tmp/javafx_win/*/* ${JAVA_WIN_MODS} && \
    \
    rm -rf /tmp/*
        
ENTRYPOINT ["/usr/local/bin/mvn-entrypoint.sh"]
CMD ["mvn"]