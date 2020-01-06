# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

FROM docker:dind
LABEL maintainer="Khosrow Moossavi <me@khosrow.io> (@khos2ow)"

RUN apk add --no-cache \
		bash \
		sudo \
		build-base \
		git \
		openjdk8 \
		ruby ruby-io-console ruby-bundler \
		python python3 python-dev py-pip \
		build-base \
		openssl \
        openssh \
		curl \
		wget \
		rsync \
		tar \
		gzip \
		zip \
		vim \
		jq \
		findutils \
		which \
	&& pip install --upgrade pip \
	&& pip install virtualenv \
	&& rm -rf /var/cache/apk/*

# maven
ENV MAVEN_VERSION 3.5.2
ENV MAVEN_HOME /usr/lib/mvn
ENV PATH ${PATH}:${MAVEN_HOME}/bin

RUN cd /usr/local && \
	wget http://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-maven-$MAVEN_VERSION-bin.tar.gz && \
	tar -zxvf apache-maven-$MAVEN_VERSION-bin.tar.gz && \
	rm -f apache-maven-$MAVEN_VERSION-bin.tar.gz && \
	mv apache-maven-$MAVEN_VERSION /usr/lib/mvn

# gradle
ENV IVY_HOME /cache
ENV GRADLE_VERSION 4.8
ENV GRADLE_HOME /usr/local/gradle
ENV PATH ${PATH}:${GRADLE_HOME}/bin

RUN cd /usr/local && \
	wget  https://downloads.gradle.org/distributions/gradle-$GRADLE_VERSION-bin.zip && \
    unzip gradle-$GRADLE_VERSION-bin.zip && \
    rm -f gradle-$GRADLE_VERSION-bin.zip && \
    ln -s gradle-$GRADLE_VERSION gradle

COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh
COPY environment-info.sh /usr/local/bin/environment-info.sh

ENTRYPOINT ["docker-entrypoint.sh"]
