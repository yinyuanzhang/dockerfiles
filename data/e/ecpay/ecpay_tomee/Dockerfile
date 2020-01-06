FROM openjdk:8-jre-alpine

RUN apk add --no-cache curl

ENV PATH /usr/local/tomee/bin:$PATH
RUN mkdir -p /usr/local/tomee

WORKDIR /usr/local/tomee
RUN curl -L https://repo.maven.apache.org/maven2/org/apache/tomee/apache-tomee/7.0.4/apache-tomee-7.0.4-plus.tar.gz -o tomee.tar.gz \
		&& tar -zxf tomee.tar.gz \
		&& mv apache-tomee-plus-7.0.4/* . \
		&& rm -Rf apache-tomee-plus-7.0.4 \
		&& rm bin/*.bat \
		&& rm tomee.tar.gz*

# Copy mysql driver
RUN curl http://repo1.maven.org/maven2/mysql/mysql-connector-java/6.0.6/mysql-connector-java-6.0.6.jar \
	-o lib/mysql-connector-java-6.0.6.jar

EXPOSE 8080
CMD ["catalina.sh", "run"]
