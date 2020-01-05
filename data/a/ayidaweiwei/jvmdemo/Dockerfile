FROM openjdk:8-jdk-alpine

EXPOSE 8888

ADD build/libs/jvmshare-0.0.1-SNAPSHOT.jar lib/jvmshare-0.0.1-SNAPSHOT.jar
# copy arthas
COPY --from=ayidaweiwei/arthas-spring-boot:latest /lib /lib

#option 1   to avoid pid = 1

# Add Tini
RUN apk add --no-cache tini
#Tini is now available at /sbin/tini
ENTRYPOINT ["/sbin/tini", "--"]
#Run demo program under Tini

ADD run.sh run.sh
CMD /run.sh

#option 2 to avoid pid = 1

#CMD ["/bin/sh","java -jar /app.jar"]









