FROM adoptopenjdk/openjdk11:jdk-11.0.3_7-slim

RUN curl -LO https://search.maven.org/remotecontent?filepath=sqlline/sqlline/1.7.0/sqlline-1.7.0-jar-with-dependencies.jar
RUN curl -LO https://search.maven.org/remotecontent?filepath=com/microsoft/sqlserver/mssql-jdbc/7.0.0.jre10/mssql-jdbc-7.0.0.jre10.jar

ENTRYPOINT ["java", "-classpath", "sqlline-1.7.0-jar-with-dependencies.jar:mssql-jdbc-7.0.0.jre10.jar", "sqlline.SqlLine"]