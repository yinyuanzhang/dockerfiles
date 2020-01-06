FROM shoepping/jenkins-ssh-slave:18.10.29

# https://github.com/keeganwitt/docker-gradle/blob/e486d3ff8bb68e77ac37239d68d4d60f4a9485fc/jdk7/Dockerfile
ENV GRADLE_HOME /opt/gradle
ENV GRADLE_VERSION 4.10.2

# https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip.sha256
ARG GRADLE_DOWNLOAD_SHA256=b49c6da1b2cb67a0caf6c7480630b51c70a11ca2016ff2f555eaeda863143a29

# https://superuser.com/questions/1423486/issue-with-fetching-http-deb-debian-org-debian-dists-jessie-updates-inrelease
RUN printf "deb http://archive.debian.org/debian/ jessie main\ndeb-src http://archive.debian.org/debian/ jessie main\ndeb http://security.debian.org jessie/updates main\ndeb-src http://security.debian.org jessie/updates main" > /etc/apt/sources.list

RUN apt-get update
RUN apt-get install -y curl zip wget

RUN apt-get install -y \
     apt-transport-https \
     ca-certificates \
     curl \
     gnupg2 \
     python-virtualenv \
     software-properties-common
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -
RUN add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/debian \
   $(lsb_release -cs) \
   stable"

RUN apt-get update
RUN apt-cache madison docker-ce
RUN apt-get install -y \
	docker-ce=18.06.3~ce~3-0~debian \
	jq

RUN usermod -aG docker jenkins

ENV DOCKER_COMPOSE_VERSION=1.24.0
RUN curl -L "https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

RUN chmod +x /usr/local/bin/docker-compose
RUN docker-compose --version


RUN set -o errexit -o nounset \
	&& echo "Downloading Gradle" \
	&& wget --no-verbose --output-document=gradle.zip "https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip" \
	\
	&& echo "Checking download hash" \
	&& echo "${GRADLE_DOWNLOAD_SHA256} *gradle.zip" | sha256sum --check - \
	\
	&& echo "Installing Gradle" \
	&& unzip gradle.zip \
	&& rm gradle.zip \
	&& mv "gradle-${GRADLE_VERSION}" "${GRADLE_HOME}/" \
	&& ln --symbolic "${GRADLE_HOME}/bin/gradle" /usr/bin/gradle


# groovy installation based on https://github.com/groovy/docker-groovy/blob/master/jdk8/Dockerfile
ENV GROOVY_HOME /opt/groovy
ENV GROOVY_VERSION 2.5.8


RUN set -o errexit -o nounset \
	&& echo "Downloading Groovy" \
	&& wget --no-verbose --output-document=groovy.zip "https://dist.apache.org/repos/dist/release/groovy/${GROOVY_VERSION}/distribution/apache-groovy-binary-${GROOVY_VERSION}.zip" \
	\
	&& echo "Importing keys listed in http://www.apache.org/dist/groovy/KEYS from key server" \
	&& echo "Installing Groovy" \
	&& unzip groovy.zip \
	&& rm groovy.zip \
	&& mv "groovy-${GROOVY_VERSION}" "${GROOVY_HOME}/" \
	&& ln --symbolic "${GROOVY_HOME}/bin/grape" /usr/bin/grape \
	&& ln --symbolic "${GROOVY_HOME}/bin/groovy" /usr/bin/groovy \
	&& ln --symbolic "${GROOVY_HOME}/bin/groovyc" /usr/bin/groovyc \
	&& ln --symbolic "${GROOVY_HOME}/bin/groovyConsole" /usr/bin/groovyConsole \
	&& ln --symbolic "${GROOVY_HOME}/bin/groovydoc" /usr/bin/groovydoc \
	&& ln --symbolic "${GROOVY_HOME}/bin/groovysh" /usr/bin/groovysh \
  && ln --symbolic "${GROOVY_HOME}/bin/java2groovy" /usr/bin/java2groovy
