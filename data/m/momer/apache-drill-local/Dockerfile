FROM drill/apache-drill:1.16.0

LABEL maintainer="momer@c-k.com"

# Should check to ensure that this matches what we expect (hash)
RUN curl https://jdbc.postgresql.org/download/postgresql-42.2.6.jar -o /opt/drill/jars/3rdparty/postgresql-42.2.6.jar

COPY conf/drill-override-example.conf /opt/drill/conf/drill-override.conf