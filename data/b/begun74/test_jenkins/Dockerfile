#FROM openjdk:8-jdk-alpine
#VOLUME /tmp
#ARG JAR_FILE
#COPY ${JAR_FILE} app.jar
#ENTRYPOINT ["java","-jar","/app.jar"]

FROM java

WORKDIR /tjapp

COPY . /tjapp

#RUN java -jar tjapp.jar

EXPOSE 8800

CMD ["java", "-jar","tjapp.jar"]
