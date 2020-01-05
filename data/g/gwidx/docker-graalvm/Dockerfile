FROM alpine:3.7 AS build

ENV GRAAL_VERSION=1.0.0-rc2
ENV GRAAL_CE_URL=https://github.com/oracle/graal/releases/download/vm-${GRAAL_VERSION}/graalvm-ce-${GRAAL_VERSION}-linux-amd64.tar.gz

RUN apk add --no-cache wget tar gzip
RUN wget -q $GRAAL_CE_URL -O graalvm-ce-linux-amd64.tar.gz
RUN tar -xvzf graalvm-ce-linux-amd64.tar.gz
RUN rm -r graalvm-ce-${GRAAL_VERSION}/man && \
    rm graalvm-ce-${GRAAL_VERSION}/src.zip
RUN mkdir -p /usr/lib/jvm
RUN mv graalvm-ce-${GRAAL_VERSION} /usr/lib/jvm/graalvm
RUN sed -i s/#networkaddress.cache.ttl=-1/networkaddress.cache.ttl=10/ /usr/lib/jvm/graalvm/jre/lib/security/java.security
RUN rm -rf /usr/lib/jvm/graalvm/*src.zip \
    /usr/lib/jvm/graalvm/lib/missioncontrol \
    /usr/lib/jvm/graalvm/lib/visualvm \
    /usr/lib/jvm/graalvm/lib/*javafx* \
    /usr/lib/jvm/graalvm/jre/plugin \
    /usr/lib/jvm/graalvm/jre/bin/javaws \
    /usr/lib/jvm/graalvm/jre/bin/jjs \
    /usr/lib/jvm/graalvm/jre/bin/orbd \
    /usr/lib/jvm/graalvm/jre/bin/pack200 \
    /usr/lib/jvm/graalvm/jre/bin/policytool \
    /usr/lib/jvm/graalvm/jre/bin/rmid \
    /usr/lib/jvm/graalvm/jre/bin/rmiregistry \
    /usr/lib/jvm/graalvm/jre/bin/servertool \
    /usr/lib/jvm/graalvm/jre/bin/tnameserv \
    /usr/lib/jvm/graalvm/jre/bin/unpack200 \
    /usr/lib/jvm/graalvm/jre/lib/javaws.jar \
    /usr/lib/jvm/graalvm/jre/lib/deploy* \
    /usr/lib/jvm/graalvm/jre/lib/desktop \
    /usr/lib/jvm/graalvm/jre/lib/*javafx* \
    /usr/lib/jvm/graalvm/jre/lib/*jfx* \
    /usr/lib/jvm/graalvm/jre/lib/amd64/libdecora_sse.so \
    /usr/lib/jvm/graalvm/jre/lib/amd64/libprism_*.so \
    /usr/lib/jvm/graalvm/jre/lib/amd64/libfxplugins.so \
    /usr/lib/jvm/graalvm/jre/lib/amd64/libglass.so \
    /usr/lib/jvm/graalvm/jre/lib/amd64/libgstreamer-lite.so \
    /usr/lib/jvm/graalvm/jre/lib/amd64/libjavafx*.so \
    /usr/lib/jvm/graalvm/jre/lib/amd64/libjfx*.so \
    /usr/lib/jvm/graalvm/jre/lib/ext/jfxrt.jar \
    /usr/lib/jvm/graalvm/jre/lib/ext/nashorn.jar \
    /usr/lib/jvm/graalvm/jre/lib/oblique-fonts \
    /usr/lib/jvm/graalvm/jre/lib/plugin.jar


FROM alpine:3.7
ENV JAVA_HOME=/usr/lib/jvm/graalvm
ENV GRAALVM_HOME=/usr/lib/jvm/graalvm
ENV PATH=$PATH:/usr/lib/jvm/graalvm/bin
ENV GLIBC_VERSION=2.27-r0

RUN wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://raw.githubusercontent.com/sgerrand/alpine-pkg-glibc/master/sgerrand.rsa.pub \
    &&  wget "https://github.com/sgerrand/alpine-pkg-glibc/releases/download/$GLIBC_VERSION/glibc-$GLIBC_VERSION.apk" \
    &&  apk --no-cache add "glibc-$GLIBC_VERSION.apk" \
    &&  rm "glibc-$GLIBC_VERSION.apk" \
    &&  wget "https://github.com/sgerrand/alpine-pkg-glibc/releases/download/$GLIBC_VERSION/glibc-bin-$GLIBC_VERSION.apk" \
    &&  apk --no-cache add "glibc-bin-$GLIBC_VERSION.apk" \
    &&  rm "glibc-bin-$GLIBC_VERSION.apk" \
    &&  wget "https://github.com/sgerrand/alpine-pkg-glibc/releases/download/$GLIBC_VERSION/glibc-i18n-$GLIBC_VERSION.apk" \
    &&  apk --no-cache add "glibc-i18n-$GLIBC_VERSION.apk" \
    && rm "glibc-i18n-$GLIBC_VERSION.apk"

COPY --from=build /usr/lib/jvm/graalvm /usr/lib/jvm/graalvm

CMD java -version
