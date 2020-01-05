FROM library/ibmjava
#RUN echo "40.89.185.28	development-shard-00-02-jf7ex.azure.mongodb.net" >> /etc/hostname
#RUN echo "20.188.35.29	development-shard-00-01-jf7ex.azure.mongodb.net" >> /etc/hostname
#RUN echo "40.89.189.248	development-shard-00-00-jf7ex.azure.mongodb.net" >> /etc/hostname
COPY target/springtesttool2-0.0.1-SNAPSHOT.jar /springtesttool2.jar
ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom","-jar","/springtesttool2.jar"]
EXPOSE 8080