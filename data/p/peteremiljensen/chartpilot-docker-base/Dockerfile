FROM amazoncorretto:8


# Add JVM default DNS ttl
RUN echo "networkaddress.cache.ttl=60" >> $JAVA_HOME/jre/lib/security/java.security

# JMX
EXPOSE 9010 
