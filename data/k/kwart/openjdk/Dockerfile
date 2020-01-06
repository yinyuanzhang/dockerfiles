#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

FROM alpine:3.10

MAINTAINER Josef (kwart) Cacek <josef.cacek@gmail.com>

ENV MAVEN_VERSION=3.6.2

COPY bashrc /root/.bashrc

RUN echo echo "Installing APK packages" \
    && apk update && apk upgrade \
    && apk add openjdk8 bash curl procps git zip bind-tools \
    && wget http://www.eu.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-maven-$MAVEN_VERSION-bin.zip \
    && unzip -q apache-maven-$MAVEN_VERSION-bin.zip -d /usr/share \
    && ln -s /usr/share/apache-maven-$MAVEN_VERSION/bin/mvn /usr/bin/mvn \
    && sed -i s#/bin/ash#/bin/bash# /etc/passwd \
    && echo "Cleaning APK cache" \
    && rm -rf /var/cache/apk/*

CMD ["/bin/bash"]
