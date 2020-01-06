FROM apribase/debian-jp
MAINTAINER apribase

#### install arangodb

RUN wget https://www.arangodb.org/repositories/arangodb2/Debian_7.0/Release.key
RUN apt-key add - < Release.key # key id: 1C42E360
RUN rm -f Release.key
RUN echo 'deb https://www.arangodb.org/repositories/arangodb2/Debian_7.0/ /' >> /etc/apt/sources.list.d/arangodb.list
RUN apt-get update
RUN apt-get install -y arangodb=2.2.2

# change arangodb uid gid
RUN groupmod -g 8529 arangodb
RUN usermod -u 8529 arangodb
RUN chown -R arangodb:arangodb /var/lib/arangodb
RUN chown -R arangodb:arangodb /var/lib/arangodb-apps
RUN chown -R arangodb:arangodb /var/log/arangodb
RUN chown -R arangodb:arangodb /var/run/arangodb

#### run
USER arangodb
WORKDIR /var/lib/arangodb

VOLUME /var/lib/arangodb
VOLUME /var/lib/arangodb-apps
VOLUME /var/log/arangodb
EXPOSE 8529

CMD ["arangod"]

# Check the README! You can boot by Puppet and Systemd.
