FROM openjdk:8
COPY . /liresolr
WORKDIR /liresolr
RUN ./gradlew distForSolr

FROM solr:7-alpine
COPY --from=0 /liresolr/dist/lire*.jar /opt/solr/server/solr-webapp/webapp/WEB-INF/lib/
