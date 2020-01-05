FROM cimadai/build_image_without_jvm

##############################
# install java (open jdk)
##############################
# Default to UTF-8 file.encoding
ENV LANG C.UTF-8

ENV GLIBC_VERSION=2.27-r0 \
    GRAALVM_VERSION=1.0.0-rc5 \
    JAVA_HOME=/usr/lib/jvm/graalvm-ce-1.0.0-rc5 \
    PATH=/usr/lib/jvm/graalvm-ce-1.0.0-rc5/bin:$PATH

RUN apk --no-cache add ca-certificates wget gcc zlib zlib-dev libc-dev

RUN mkdir /usr/lib/jvm; \
    wget "https://github.com/oracle/graal/releases/download/vm-${GRAALVM_VERSION}/graalvm-ce-${GRAALVM_VERSION}-linux-amd64.tar.gz"; \
    tar -zxC /usr/lib/jvm -f graalvm-ce-${GRAALVM_VERSION}-linux-amd64.tar.gz; \
    rm -f graalvm-ce-${GRAALVM_VERSION}-linux-amd64.tar.gz

RUN wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://github.com/sgerrand/alpine-pkg-glibc/releases/download/${GLIBC_VERSION}/sgerrand.rsa.pub \
    &&  wget "https://github.com/sgerrand/alpine-pkg-glibc/releases/download/${GLIBC_VERSION}/glibc-${GLIBC_VERSION}.apk" \
    &&  wget "https://github.com/sgerrand/alpine-pkg-glibc/releases/download/${GLIBC_VERSION}/glibc-bin-${GLIBC_VERSION}.apk" \
    &&  wget "https://github.com/sgerrand/alpine-pkg-glibc/releases/download/${GLIBC_VERSION}/glibc-i18n-${GLIBC_VERSION}.apk"

RUN  apk --no-cache add "glibc-$GLIBC_VERSION.apk" \
    &&  apk --no-cache add "glibc-bin-$GLIBC_VERSION.apk" \
    &&  apk --no-cache add "glibc-i18n-$GLIBC_VERSION.apk"

RUN  rm "glibc-$GLIBC_VERSION.apk" \
    &&  rm "glibc-bin-$GLIBC_VERSION.apk" \
    &&  rm "glibc-i18n-$GLIBC_VERSION.apk"

##############################
# install sbt
##############################
ENV SBT_VERSION 0.13.15
ENV SBT_HOME /usr/local/sbt
ENV PATH ${PATH}:${SBT_HOME}/bin

# Install sbt
RUN apk add --no-cache --update bash wget && \
    apk --update add tar && \
    mkdir -p "$SBT_HOME" && \
    wget -qO - "https://github.com/sbt/sbt/releases/download/v$SBT_VERSION/sbt-$SBT_VERSION.tgz" | tar xz -C $SBT_HOME --strip-components=1 && \
    echo -ne "- with sbt $SBT_VERSION\n" >> /root/.built && \
    /usr/local/sbt/bin/sbt sbtVersion

