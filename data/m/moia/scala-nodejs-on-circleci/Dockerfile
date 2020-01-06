# Dockerfile that contains
# - Scala (from base image)
# - AWS CLI (from base image)
# - kubectl (from base image)
# - sonar-scanner (from base image)
# - Java 8 JDK (from base image)
# - SBT (from base image)
# - Docker (from base image)
# - NodeJS

# Pull base image (https://github.com/moia-dev/scala-on-circleci)
# https://github.com/moia-dev/scala-on-circleci/blob/master/Dockerfile
FROM moia/scala-on-circleci:8u222-2.12.9

RUN wget https://nodejs.org/dist/v10.16.3/node-v10.16.3-linux-x64.tar.xz && \
    echo 'd2271fd8cf997fa7447d638dfa92749ff18ca4b0d796bf89f2a82bf7800d5506  node-v10.16.3-linux-x64.tar.xz' | sha256sum -c - && \
    tar -xf node-v10.16.3-linux-x64.tar.xz

ENV PATH="/home/circleci/node-v10.16.3-linux-x64/bin:$PATH"
