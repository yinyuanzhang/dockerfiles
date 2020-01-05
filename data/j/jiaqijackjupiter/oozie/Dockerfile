# Copyright 刘珈奇
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

FROM jiaqijackjupiter/hadoop

LABEL maintainer="刘珈奇"
LABEL maintainer-email="2257440489@qq.com"

ARG OOZIE_VERSION=4.3.1

# $OOZIE_HOME is computed automatically when oozie server starts
# So don't set $OOZIE_HOME anywhere
RUN mkdir /oozie
ENV OOZIE_DIR=/oozie

############################################## Install auxiliary packages ##############################################

RUN apt-get update
RUN apt-get install maven -y
RUN apt-get install unzip -y
RUN apt-get install zip -y

#################################################### Download Oozie ####################################################

# Download source
RUN wget https://archive.apache.org/dist/oozie/$OOZIE_VERSION/oozie-$OOZIE_VERSION.tar.gz
RUN tar -xvzf oozie-$OOZIE_VERSION.tar.gz
RUN rm oozie-$OOZIE_VERSION.tar.gz

# Rename extracted dir to "oozie-source"
RUN mv oozie-$OOZIE_VERSION oozie-source

# $OOZIE_SOURCE_DIR contains source code to build oozie server WAR file
ENV OOZIE_SOURCE_DIR=/oozie-source

# Move source to dedicated oozie dir
RUN mv $OOZIE_SOURCE_DIR $OOZIE_DIR

##################################################### Build Oozie ######################################################

# Override Oozie server config
ADD oozie-site.xml $OOZIE_DIR/$OOZIE_SOURCE_DIR/core/src/main/conf/oozie-site.xml

# Build with -Puber which will bundle the required hadoop and hcatalog libraries in the oozie war
# Skip tests for quicker build
# In order to use sqoop with oozie locally: -Dsqoop.version=1.4.7 -Dsqoop.classifier=hadoop260 -PUber
RUN $OOZIE_DIR/$OOZIE_SOURCE_DIR/bin/mkdistro.sh -DskipTests -Puber -Dsqoop.version=1.4.7 -Dsqoop.classifier=hadoop260

################################################# Install Oozie server #################################################

# Copy the Oozie binary package to a dedicated dir
RUN cp $OOZIE_DIR/$OOZIE_SOURCE_DIR/distro/target/oozie-$OOZIE_VERSION-distro.tar.gz .
RUN tar -xzvf oozie-$OOZIE_VERSION-distro.tar.gz
RUN rm oozie-$OOZIE_VERSION-distro.tar.gz
RUN mv oozie-$OOZIE_VERSION /oozie-server

ENV OOZIE_SERVER_DIR=/oozie-server

# $OOZIE_DIR/$OOZIE_SERVER_DIR has both Oozie server and complete Oozie binary of everything
RUN mv $OOZIE_SERVER_DIR $OOZIE_DIR

# Collect third-party libraries
# ExtJS
RUN mkdir $OOZIE_DIR/$OOZIE_SERVER_DIR/libext/
RUN cd $OOZIE_DIR/$OOZIE_SERVER_DIR/libext/ && wget http://archive.cloudera.com/gplextras/misc/ext-2.2.zip

# Create a self-contained Oozie WAR file
RUN $OOZIE_DIR/$OOZIE_SERVER_DIR/bin/oozie-setup.sh prepare-war

# Create the Oozie DB
RUN $OOZIE_DIR/$OOZIE_SERVER_DIR/bin/ooziedb.sh create -sqlfile oozie.sql -run

################################################# Install Oozie Client #################################################

RUN cp $OOZIE_DIR/$OOZIE_SERVER_DIR/oozie-client-$OOZIE_VERSION.tar.gz .
RUN tar -xzvf oozie-client-$OOZIE_VERSION.tar.gz
RUN rm oozie-client-$OOZIE_VERSION.tar.gz
RUN mv oozie-client-$OOZIE_VERSION /oozie-client

ENV OOZIE_CLIENT_DIR=/oozie-client

RUN mv $OOZIE_CLIENT_DIR $OOZIE_DIR

ENV PATH=$OOZIE_DIR/$OOZIE_CLIENT_DIR/bin:$PATH

################################################# Setup Container init #################################################

ADD oozie-init.sh /etc/oozie-init.sh
RUN chown root:root /etc/oozie-init.sh
RUN chmod 700 /etc/oozie-init.sh
ENV INIT /etc/oozie-init.sh

RUN mkdir /example
COPY example/* /example/
