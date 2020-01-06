FROM azul/zulu-openjdk-alpine:11 as jdk
RUN jlink \
    --module-path /usr/lib/jvm/*/jmods/ \
    --verbose \
    --add-modules java.base,java.logging,java.xml,jdk.unsupported,java.naming,jdk.zipfs,java.sql,java.desktop \
    --compress 2 \
    --no-header-files \
    --no-man-pages \
    --output /opt/jdk-11-minimal

FROM alpine:3.8
ENV JAVA_HOME=/opt/jdk-11-minimal
ENV PATH=$PATH:/opt/jdk-11-minimal/bin
COPY --from=jdk /opt/jdk-11-minimal /opt/jdk-11-minimal
