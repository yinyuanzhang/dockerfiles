FROM maven:3.5-jdk-8 AS BUILD_IMAGE
WORKDIR /root/
RUN git clone https://github.com/denisdbell/spring-petclinic.git
WORKDIR /root/spring-petclinic/
RUN mvn clean package -DskipTests


FROM openjdk:8
WORKDIR /root/
VOLUME ["/root/log"]
COPY --from=BUILD_IMAGE /root/spring-petclinic/target/*.jar .
CMD java -jar "$(echo *.jar)"

EXPOSE 8080