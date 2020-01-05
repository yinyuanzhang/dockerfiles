FROM alpine:3.2

ENV JAVA_VERSION=8
ENV JAVA_UPDATE=66
ENV JAVA_BUILD=17
ENV JAVA_HOME=/usr/lib/jvm/default-jvm
ENV JAVA_TOOL_OPTIONS=-Dfile.encoding=UTF8

RUN apk add -U libc6-compat wget sudo openssh-client git \
	&& wget -O /tmp/glibc.apk "https://github.com/sgerrand/alpine-pkg-glibc/releases/download/unreleased/glibc-2.23-r3.apk" \
	&& apk add --allow-untrusted /tmp/glibc.apk \
	&& /sbin/ldconfig /lib /usr/glibc/usr/lib \
	&& rm /tmp/glibc.apk \
	&& rm -rf /var/cache/apk/*

# Java
RUN apk add --update wget ca-certificates \
		&& cd /tmp \
		&& wget --header "Cookie: oraclelicense=accept-securebackup-cookie;" \
				"http://download.oracle.com/otn-pub/java/jdk/${JAVA_VERSION}u${JAVA_UPDATE}-b${JAVA_BUILD}/jdk-${JAVA_VERSION}u${JAVA_UPDATE}-linux-x64.tar.gz" \
		&& tar xzf "jdk-${JAVA_VERSION}u${JAVA_UPDATE}-linux-x64.tar.gz" \
		&& mkdir -p "/usr/lib/jvm" \
		&& mv "/tmp/jdk1.${JAVA_VERSION}.0_${JAVA_UPDATE}" "/usr/lib/jvm/java-${JAVA_VERSION}-oracle" \
		&& ln -s "java-${JAVA_VERSION}-oracle" "$JAVA_HOME" \
		&& ln -s "$JAVA_HOME/bin/"* "/usr/bin/" \
		&& rm -rf "$JAVA_HOME/"*src.zip \
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
					 "$JAVA_HOME/jre/lib/amd64/"libjfx*.so \
		&& apk del wget ca-certificates \
		&& rm /tmp/* /var/cache/apk/*

ENTRYPOINT []
CMD ["java", "-version"]
