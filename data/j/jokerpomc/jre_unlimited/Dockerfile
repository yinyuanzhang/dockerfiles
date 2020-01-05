# AlpineLinux with a glibc-2.29-r0 and Oracle Java 8
FROM alpine:3.8

MAINTAINER wang.jun@rongzer.com

# Java Version and other ENV
ENV JAVA_VERSION_MAJOR=8 \
    JAVA_VERSION_MINOR=231 \
    JAVA_VERSION_BUILD=11 \
    JAVA_PACKAGE=jre \
    JAVA_JCE=unlimited \
    JAVA_HOME=/opt/java \
    PATH=${PATH}:/opt/java/bin \
    GLIBC_REPO=https://github.com/sgerrand/alpine-pkg-glibc \
    GLIBC_VERSION=2.30-r0 \
    LANG=C.UTF-8

COPY ./jre-8u231-linux-x64.tar.gz /tmp/java.tar.gz
# do all in one step
RUN set -ex && \
    [[ ${JAVA_VERSION_MAJOR} != 7 ]] || ( echo >&2 'Oracle no longer publishes JAVA7 packages' && exit 1 ) && \
    apk -U upgrade && \
    apk add libstdc++ curl ca-certificates bash && \
    wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub && \
    for pkg in glibc-${GLIBC_VERSION} glibc-bin-${GLIBC_VERSION} glibc-i18n-${GLIBC_VERSION}; do curl -sSL ${GLIBC_REPO}/releases/download/${GLIBC_VERSION}/${pkg}.apk -o /tmp/${pkg}.apk; done && \
    apk add /tmp/*.apk && \
    rm -v /tmp/*.apk && \
    ( /usr/glibc-compat/bin/localedef --force --inputfile POSIX --charmap UTF-8 C.UTF-8 || true ) && \
    echo "export LANG=C.UTF-8" > /etc/profile.d/locale.sh  && \
    /usr/glibc-compat/sbin/ldconfig /lib /usr/glibc-compat/lib && \
    mkdir /opt && \
    gunzip /tmp/java.tar.gz && \
    tar -C /opt -xf /tmp/java.tar && \
    ln -s /opt/jre1.${JAVA_VERSION_MAJOR}.0_${JAVA_VERSION_MINOR} /opt/java && \
    if [ "${JAVA_JCE}" == "unlimited" ]; then echo "Installing Unlimited JCE policy" && \
      curl -jksSLH "Cookie: oraclelicense=accept-securebackup-cookie" -o /tmp/jce_policy-${JAVA_VERSION_MAJOR}.zip \
        http://download.oracle.com/otn-pub/java/jce/${JAVA_VERSION_MAJOR}/jce_policy-${JAVA_VERSION_MAJOR}.zip && \
      cd /tmp && unzip /tmp/jce_policy-${JAVA_VERSION_MAJOR}.zip && \
      mv /tmp/UnlimitedJCEPolicyJDK8/*.jar /opt/java/lib/security/; \
    fi && \
    sed -i s/#networkaddress.cache.ttl=-1/networkaddress.cache.ttl=10/ $JAVA_HOME/lib/security/java.security && \
    apk add tzdata && \
    ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    echo "Etc/Asia/Shanghai" > /etc/timezone && \
    apk del curl glibc-i18n && \
    rm -rf /var/cache/apk/ \
            /tmp/* \
            /opt/java/lib/plugin.jar \
            /opt/java/lib/ext/jfxrt.jar \
            /opt/java/bin/javaws \
            /opt/java/lib/javaws.jar \
            /opt/java/lib/desktop \
            /opt/java/plugin \
            /opt/java/lib/deploy* \
            /opt/java/lib/*javafx* \
            /opt/java/lib/*jfx* \
            /opt/java/lib/amd64/libdecora_sse.so \
            /opt/java/lib/amd64/libprism_*.so \
            /opt/java/lib/amd64/libfxplugins.so \
            /opt/java/lib/amd64/libglass.so \
            /opt/java/lib/amd64/libgstreamer-lite.so \
            /opt/java/lib/amd64/libjavafx*.so \
            /opt/java/lib/amd64/libjfx*.so && \
    ln -sf /etc/ssl/certs/java/cacerts $JAVA_HOME/lib/security/cacerts && \
    echo 'hosts: files mdns4_minimal [NOTFOUND=return] dns mdns4' >> /etc/nsswitch.conf

# EOF

