FROM openjdk:8-jre
MAINTAINER chaya

#Install postgres client, to check database state
RUN apt-get update && apt-get install -y postgresql-client

COPY run.sh /usr/local/bin/run.sh
RUN chmod +x /usr/local/bin/run.sh
CMD ["run.sh"]