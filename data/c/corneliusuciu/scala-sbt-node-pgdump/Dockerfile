#
# Scala, sbt, Node.js and pg_dump Dockerfile
#
# https://github.com/corneliusuciu/scala-sbt-node-pgdump
#

# Pull base image
FROM hseeberger/scala-sbt:8u181_2.12.8_1.2.8

# Install Node.js
RUN \
  curl -sL https://deb.nodesource.com/setup_10.x | bash - && \
  apt-get update && \
  DEBIAN_FRONTEND=noninteractive apt-get -yq --no-install-recommends --force-yes install nodejs

# Install pg_dump
RUN \
  DEBIAN_FRONTEND=noninteractive apt-get -yq --no-install-recommends --force-yes install curl ca-certificates && \
  curl https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - && \
  sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ stretch-pgdg main" > /etc/apt/sources.list.d/pgdg.list' && \
  apt-get update && \
  DEBIAN_FRONTEND=noninteractive apt-get -yq --no-install-recommends --force-yes install postgresql-client-10

# Define working directory
WORKDIR /root
