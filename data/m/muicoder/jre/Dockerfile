FROM muicoder/glibc

ENV JAVA_HOME=/opt/jdk
ENV JRE_HOME=$JAVA_HOME/jre
ENV CLASSPATH=.:$JAVA_HOME/lib:$JRE_HOME/lib

ENV PATH=$JAVA_HOME/bin:$JRE_HOME/bin:$PATH

RUN JAVA_VERSION_MAJOR=8 \
    JAVA_VERSION_MINOR=121 \
    JAVA_VERSION_BUILD=13 \
    JAVA_PACKAGE=server-jre \
    JAVA_JCE=unlimited && \
    mkdir /opt && \
        curl -jksSLH "Cookie: oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-b${JAVA_VERSION_BUILD}/e9e7ea248e2c4826b92b3f075a80e441/${JAVA_PACKAGE}-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.tar.gz \
            -o /tmp/${JAVA_PACKAGE}-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.tar.gz && \
        tar -C /opt -xf /tmp/${JAVA_PACKAGE}-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.tar.gz && \
        mv /opt/jdk1.${JAVA_VERSION_MAJOR}.0_${JAVA_VERSION_MINOR} $JAVA_HOME && \
        if [ "${JAVA_JCE}" == "unlimited" ]; then echo "Installing Unlimited JCE policy" && \
            curl -jksSLH "Cookie: oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jce/${JAVA_VERSION_MAJOR}/jce_policy-${JAVA_VERSION_MAJOR}.zip \
                -o /tmp/jce_policy-${JAVA_VERSION_MAJOR}.zip && \
            unzip /tmp/jce_policy-${JAVA_VERSION_MAJOR}.zip -d /tmp && \
            mv /tmp/UnlimitedJCEPolicyJDK${JAVA_VERSION_MAJOR}/*.jar $JRE_HOME/lib/security; \
        fi && \
    rm -rf /tmp/*

CMD ["java", "-version"]
