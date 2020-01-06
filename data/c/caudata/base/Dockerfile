FROM node:10-slim
LABEL maintainer="caudata <admin@caudata.io>"

###### DISCLAIMER ######
#
# You must accept the Oracle Binary Code License Agreement for Java SE to use this image.
#
# Link to License: http://www.oracle.com/technetwork/java/javase/terms/license/index.html
#
###### DISCLAIMER ######

# Set java enviroment
ENV LANG=C.UTF-8 \ 
	JAVA_MAJOR_VERSION=10 \
	JAVA_MINOR_VERSION=0 \
	JAVA_UPDATE=2 \
	JAVA_BUILD=13 \
	JAVA_PATH=19aef61b38124481863b1413dce1855f \
	JAVA_TYPE=jdk

ENV JAVA_FULL_VERSION="${JAVA_MAJOR_VERSION}.${JAVA_MINOR_VERSION}.${JAVA_UPDATE}"

ENV JAVA_HOME="/opt/java/${JAVA_TYPE}-${JAVA_FULL_VERSION}" \
	JAVA_TAR="${JAVA_TYPE}-${JAVA_FULL_VERSION}_linux-x64_bin.tar.gz"

# Downloading oracle jdk -> extract it -> cleanup -> add app user & group
# You can use USER called 'app' for your application
RUN cd /tmp \
	&& apt-get update \
	&& apt-get install -y wget \
	&& mkdir -p $JAVA_HOME \
	&& wget --header "Cookie: oraclelicense=accept-securebackup-cookie;" \
	--progress=dot:mega --tries=10 "http://download.oracle.com/otn-pub/java/jdk/${JAVA_FULL_VERSION}+${JAVA_BUILD}/${JAVA_PATH}/${JAVA_TAR}" \
	&& tar -xzf $JAVA_TAR -C /opt/java \
	&& ln -s $JAVA_HOME $JAVA_HOME/bin/* /usr/bin/ \
	&& rm -rf $JAVA_HOME/lib/src.zip \
	$JAVA_HOME/lib/missioncontrol \
	$JAVA_HOME/lib/*javafx* \
	$JAVA_HOME/lib/*jfx* \
	$JAVA_HOME/lib/*awt* \
	$JAVA_HOME/lib/desktop \
	$JAVA_HOME/lib/javaws.jar \
	$JAVA_HOME/lib/plugin.jar \
	$JAVA_HOME/lib/plugin-legacy.jar \
	$JAVA_HOME/lib/javaws.jar \
	$JAVA_HOME/lib/desktop \
	$JAVA_HOME/lib/deploy \
	$JAVA_HOME/lib/deploy* \
	$JAVA_HOME/lib/fonts \
	$JAVA_HOME/lib/oblique-fonts \
	$JAVA_HOME/jmods \
    && apt-get clean -y \
    && apt-get autoremove -y \
    && apt-get autoclean -y \
    && rm -rf /tmp/* \
    && rm -rf /var/cache/apt/archives/* \
	&& useradd -ms /bin/bash app

# Add java to path
ENV PATH $PATH:$JAVA_HOME/bin


ENV LEIN_VERSION=2.8.1
ENV LEIN_INSTALL=/usr/local/bin/

WORKDIR /tmp

# Download the whole repo as an archive
RUN mkdir -p $LEIN_INSTALL \
  && wget -q https://raw.githubusercontent.com/technomancy/leiningen/$LEIN_VERSION/bin/lein-pkg \
  && mv lein-pkg $LEIN_INSTALL/lein \
  && chmod 0755 $LEIN_INSTALL/lein \
  && wget -q https://github.com/technomancy/leiningen/releases/download/$LEIN_VERSION/leiningen-$LEIN_VERSION-standalone.zip \
  && mkdir -p /usr/share/java \
  && mv leiningen-$LEIN_VERSION-standalone.zip /usr/share/java/leiningen-$LEIN_VERSION-standalone.jar

ENV PATH=$PATH:$LEIN_INSTALL
ENV LEIN_ROOT 1

COPY ./project.clj .
RUN lein deps
RUN apt update && apt install -y ocl-icd-opencl-dev

# RUN apt install -y ocl-icd-opencl-dev
# COPY ./shadow-cljs.edn .
# RUN npm install -g shadow-cljs yarn
# RUN shadow-cljs check

