#-------------------------------------------------------------------------------
# Copyright (C) 2015 The Gravitee team (http://gravitee.io)
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#            http://www.apache.org/licenses/LICENSE-2.0
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
#-------------------------------------------------------------------------------
FROM graviteeio/java:8
MAINTAINER Gravitee Team <http://gravitee.io>

ARG GRAVITEEIO_VERSION=0

# Update to get support for Zip/Unzip, nc and wget
RUN apk add --update zip unzip netcat-openbsd wget

COPY gravitee.yml startup.sh /tmp/

RUN wget https://download.gravitee.io/graviteeio-apim/distributions/graviteeio-full-${GRAVITEEIO_VERSION}.zip --no-check-certificate -P /tmp/ \
    && unzip /tmp/graviteeio-full-${GRAVITEEIO_VERSION}.zip -d /tmp/ \
    && mv /tmp/graviteeio-full-${GRAVITEEIO_VERSION}/graviteeio-gateway* /opt/graviteeio-gateway \
    && wget https://oss.sonatype.org/content/groups/public/com/loopfor/zookeeper/zookeeper-cli/1.4/zookeeper-cli-1.4.zip  --no-check-certificate -P /tmp/ \
    && unzip /tmp/zookeeper-cli-1.4.zip -d /tmp/ \    
    && mv /tmp/zookeeper-cli-1.4 /opt/ \
    && chmod +x /opt/zookeeper-cli-1.4/bin/zk \
    && mv /tmp/startup.sh /opt/graviteeio-gateway/bin/ \
    && chmod +x /opt/graviteeio-gateway/bin/startup.sh \
    && mv /tmp/gravitee.yml /opt/graviteeio-gateway/config/ \
    && rm -rf /tmp/*

ENV GRAVITEEIO_HOME /opt/graviteeio-gateway

WORKDIR ${GRAVITEEIO_HOME}

EXPOSE 8082
VOLUME ["/opt/graviteeio-gateway/logs"]
CMD ["./bin/startup.sh"]
