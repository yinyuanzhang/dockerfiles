FROM sjansen/java:oracle-java8
MAINTAINER Stuart Jansen <sjansen@buscaluz.org>

COPY src/prep src/prep.d/* /tmp/
RUN /tmp/prep

CMD ["/usr/local/bin/start-cassandra"]
EXPOSE 7000 7001 7199 9042 9160
VOLUME ["/var/lib/cassandra"]

COPY src/build src/build.d/* /tmp/
RUN /tmp/build
