FROM openjdk:8-jre
MAINTAINER chaya

#Install postgres client, to check database state
RUN apt-get update && apt-get install -y postgresql-client

RUN mkdir /app
RUN chmod 777 /app
COPY run.sh /run.sh
RUN chmod +x /run.sh
CMD ["/run.sh"]