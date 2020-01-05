FROM oraclelinux:7-slim

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

ENV JAVA_TEMP /usr/java/openjdk-11-temp
ENV JAVA_HOME /usr/java/openjdk-11
ENV PATH $JAVA_HOME/bin:$PATH

# https://jdk.java.net/
ENV JAVA_VERSION 11.0.2
ENV JAVA_URL https://download.java.net/java/GA/jdk11/9/GPL/openjdk-11.0.2_linux-x64_bin.tar.gz
ENV JAVA_SHA256 99be79935354f5c0df1ad293620ea36d13f48ec3ea870c838f20c504c9668b57