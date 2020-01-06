FROM java:8

MAINTAINER Fredrik Stock <fredrik@eltele.no>

ENV VERSION=1.4.0 \
    JAVA_MX=1G

ADD https://repo1.maven.org/maven2/org/opentripplanner/otp/$VERSION/otp-$VERSION-shaded.jar /usr/local/share/java/
#MKDIR /var/otp/graphs/norway
#ADD https://storage.googleapis.com/marduk-production/outbound/gtfs/rb_norway-aggregated-gtfs.zip /var/otp/graphs/norway/
RUN ln -s otp-$VERSION-shaded.jar /usr/local/share/java/otp.jar

COPY otp /usr/local/bin/
RUN chmod 755 /usr/local/bin/*

EXPOSE 8080

CMD ["/bin/bash"]
