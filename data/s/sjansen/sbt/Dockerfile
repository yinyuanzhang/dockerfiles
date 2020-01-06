FROM sjansen/java:oracle-java8
MAINTAINER Stuart Jansen <sjansen@buscaluz.org>

COPY src/prep src/prep.d/* /tmp/
RUN /tmp/prep

VOLUME ["/app"]
WORKDIR /app

COPY src/build src/build.d/* /tmp/
RUN /tmp/build
