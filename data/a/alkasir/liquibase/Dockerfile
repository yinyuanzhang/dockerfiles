from java:7
maintainer Thomas Frössman<thomasf@jossystem.se>

add lib/liquibase-*-bin.tar.gz /liquibase
run chmod +x /liquibase/liquibase && \
    ln -s /liquibase/liquibase /usr/local/bin/
copy lib/postgresql*.jar /postgresql.jar
add bin/ /bin/

env LIQUIBASE_HOME /liquibase
volume ["/changelogs"]
workdir /
entrypoint ["/bin/lb"]
