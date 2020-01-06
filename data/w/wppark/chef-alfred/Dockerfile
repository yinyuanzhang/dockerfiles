FROM rainist/sbt:1.1.5

MAINTAINER rainist <rainist@rainist.com>

ENV ALFRED_ENV prod

RUN mkdir -p /var/www

ADD . /var/www

WORKDIR /var/www
RUN cp database.conf src/main/resources/database.conf
RUN sbt compile
RUN sbt assembly

EXPOSE 8080

CMD ["java", "-javaagent:newrelic/newrelic.jar", "-jar", "/var/www/target/scala-2.12/alfred.jar"]
