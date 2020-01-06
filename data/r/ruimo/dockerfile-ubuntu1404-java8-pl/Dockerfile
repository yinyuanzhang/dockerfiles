FROM ruimo/dockerfile-ubuntu1404-jdk8
MAINTAINER Shisei Hanai<ruimo.uno@gmail.com>

RUN apt-get install -u unzip
RUN cd /tmp && wget http://downloads.typesafe.com/typesafe-activator/1.2.3/typesafe-activator-1.2.3.zip
RUN cd /tmp && unzip -q typesafe-activator-1.2.3.zip
RUN mv /tmp/activator-1.2.3 /opt/
RUN ln -s /opt/activator-1.2.3/activator /usr/local/bin/

# Create dummy project to download artifacts.
RUN cd /tmp && \
  activator new test play-scala

RUN cd /tmp/test && \
  activator compile

RUN rm -rf /tmp/test
RUN chmod 777 /opt/activator-1.2.3/activator

EXPOSE 9000

ADD profile /profile

# Define mountable directories.
VOLUME ["/var/home"]

CMD ["/bin/bash", "--rcfile", "/profile", "-i"]
