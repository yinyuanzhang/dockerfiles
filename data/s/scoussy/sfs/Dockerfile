FROM frolvlad/alpine-glibc:alpine-3.5

ENV JAVA_VERSION=8 \
    JAVA_HOME="/usr/lib/jvm/default-jvm"

RUN	apk add --no-cache --virtual=build-dependencies wget ca-certificates && \ 
	cd "/tmp"  && \
	wget -q http://www.oracle.com/technetwork/java/javase/downloads/index.html -O index.html && \
	cat index.html | grep -Eoi '/technetwork/java/javase/downloads/jdk8-downloads-[0-9]+.html' | (head -n 1) | awk '{print "http://www.oracle.com"$1}' | xargs wget -q --no-cookies --header "Cookie: gpw_e24=xxx; oraclelicense=accept-securebackup-cookie;" -O index2.html && \
	cat index2.html | grep -Eoi '"filepath":"[^"]+jdk-8u[0-9]+-linux-x64.tar.gz"' | grep -Eoi 'http:[^"]+' | xargs wget -q --no-cookies --header "Cookie: gpw_e24=xxx; oraclelicense=accept-securebackup-cookie;" -O "jdk-${JAVA_VERSION}-linux-x64.tar.gz" && \
 	tar -xzf "jdk-${JAVA_VERSION}-linux-x64.tar.gz" && \
	mkdir -p "/usr/lib/jvm" && \ 
	mv ./jdk1.${JAVA_VERSION}* /usr/lib/jvm/java-${JAVA_VERSION}-oracle && \
	ln -s "java-${JAVA_VERSION}-oracle" "$JAVA_HOME" && \
    ln -s "$JAVA_HOME/bin/"* "/usr/bin/" && \
    wget -q --header "Cookie: oraclelicense=accept-securebackup-cookie;" \
        "http://download.oracle.com/otn-pub/java/jce/${JAVA_VERSION}/jce_policy-${JAVA_VERSION}.zip" && \
    unzip jce_policy-${JAVA_VERSION}.zip && \
	cp -v UnlimitedJCEPolicyJDK8/* $JAVA_HOME/jre/lib/security/ && \
	rm -rf UnlimitedJCEPolicy* && \
    rm -rf "$JAVA_HOME/"*src.zip && \
    rm -rf "$JAVA_HOME/lib/missioncontrol" \
           "$JAVA_HOME/lib/visualvm" \
           "$JAVA_HOME/lib/"*javafx* \
           "$JAVA_HOME/jre/lib/plugin.jar" \
           "$JAVA_HOME/jre/lib/ext/jfxrt.jar" \
           "$JAVA_HOME/jre/bin/javaws" \
           "$JAVA_HOME/jre/lib/javaws.jar" \
           "$JAVA_HOME/jre/lib/desktop" \
           "$JAVA_HOME/jre/plugin" \
           "$JAVA_HOME/jre/lib/"deploy* \
           "$JAVA_HOME/jre/lib/"*javafx* \
           "$JAVA_HOME/jre/lib/"*jfx* \
           "$JAVA_HOME/jre/lib/amd64/libdecora_sse.so" \
           "$JAVA_HOME/jre/lib/amd64/"libprism_*.so \
           "$JAVA_HOME/jre/lib/amd64/libfxplugins.so" \
           "$JAVA_HOME/jre/lib/amd64/libglass.so" \
           "$JAVA_HOME/jre/lib/amd64/libgstreamer-lite.so" \
           "$JAVA_HOME/jre/lib/amd64/"libjavafx*.so \
           "$JAVA_HOME/jre/lib/amd64/"libjfx*.so && \
    rm "${JAVA_HOME}/jre/lib/security/README.txt" && \
    apk del build-dependencies && \
    rm -rf "/tmp/"* && \
    rm -rf "/var/cache/apk/"*

ARG MAVEN_VERSION=3.3.9
ARG USER_HOME_DIR="/root"
RUN apk add --no-cache --virtual=build-dependencies curl tar && \
    mkdir -p /usr/share/maven /usr/share/maven/ref && \
    curl -fsSL http://apache.osuosl.org/maven/maven-3/$MAVEN_VERSION/binaries/apache-maven-$MAVEN_VERSION-bin.tar.gz | \
    tar -xzC /usr/share/maven --strip-components=1 && \
    ln -s /usr/share/maven/bin/mvn /usr/bin/mvn && \
    apk del build-dependencies && \
    apk add --no-cache fuse && \
    rm -rf "/tmp/"* && \
    rm -rf "/var/cache/apk/"*

ENV MAVEN_HOME /usr/share/maven
ENV MAVEN_CONFIG "$USER_HOME_DIR/.m2"
COPY settings-docker.xml /usr/share/maven/ref/

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
ADD . /usr/src/app
RUN mvn install

RUN cp -p /usr/src/app/fuse.conf /etc/fuse.conf && \
    cp -p /usr/src/app/target/sfs-0.0.1-SNAPSHOT.jar /sfs.jar && \
    cp -p /usr/src/app/entrypoint.sh /entrypoint.sh && \
    dos2unix /entrypoint.sh && chmod +x /entrypoint.sh && \
    dos2unix /etc/fuse.conf && \
    rm -R /usr/src/app "$USER_HOME_DIR/.m2" 

WORKDIR /

ENTRYPOINT ["/entrypoint.sh"]
