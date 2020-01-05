FROM java:8
LABEL maintainer="Dariusz Abramczyk"
COPY ./mysql-connector-java-8.0.13.jar mysql-connector-java-8.0.13.jar
COPY ./mysqldb.java mysqldb.java
RUN ["javac", "mysqldb.java"]
CMD ["java", "-cp", ".:mysql-connector-java-8.0.13.jar", "MySqlDB"]