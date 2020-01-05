FROM java:8

MAINTAINER Andy S Alic <asalic@upv.es>

ENV JAVA_MX=1G \
    DOWNLOAD_LINK=https://repo1.maven.org/maven2/org/opentripplanner/otp/1.2.0/otp-1.2.0-shaded.jar

ADD $DOWNLOAD_LINK /usr/local/share/java/otp.jar
RUN ln -s /usr/local/share/java/otp.jar /usr/local/bin/

COPY otp /usr/local/bin/
RUN chmod 755 /usr/local/bin/*

EXPOSE 8080
