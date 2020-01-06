# Copyright 2015 Telefónica Investigación y Desarrollo, S.A.U
#
# This file is part of the IoT Agent for the Ultralight 2.0 protocol (IOTAUL) component
#
# IOTAUL is free software: you can redistribute it and/or
# modify it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the License,
# or (at your option) any later version.
#
# IOTAUL is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public
# License along with IOTAUL.
# If not, see http://www.gnu.org/licenses/.
#
# For those usages not covered by the GNU Affero General Public License
# please contact with: [daniel.moranjimenez@telefonica.com]

FROM centos:7

MAINTAINER Daniel Moran Jimenez <daniel.moranjimenez@telefonica.com>

ARG NODEJS_VERSION=4.8.4

COPY . /opt/iotaul/
WORKDIR /opt/iotaul

RUN yum update -y && \
  yum install -y epel-release && yum update -y epel-release && \
  echo "INFO: Building node and npm..." && \
  yum install -y gcc-c++ make yum-utils git && \
  # If we not define node version, use the official for the SO
  [[ "${NODEJS_VERSION}" == "" ]] && export NODEJS_VERSION="$(repoquery --qf '%{VERSION}' nodejs.x86_64)" || echo "INFO: Using specific node version..." && \
  echo "***********************************************************" && \
  echo "USING NODEJS VERSION <${NODEJS_VERSION}>" && \
  echo "***********************************************************" && \
  curl -s --fail http://nodejs.org/dist/v${NODEJS_VERSION}/node-v${NODEJS_VERSION}.tar.gz -o /opt/node-v${NODEJS_VERSION}.tar.gz && \
  tar zxf /opt/node-v${NODEJS_VERSION}.tar.gz -C /opt && \
  cd /opt/node-v${NODEJS_VERSION} && \
  echo "INFO: Configure..." && ./configure && \
  echo "INFO: Make..." && make -s V= && \
  echo "INFO: Make install..." && make install && \
  echo "INFO: node version <$(node -e "console.log(process.version)")>" && \
  echo "INFO: npm version <$(npm --version)>" && \
  echo "INFO: npm install --production..." && \
  cd /opt/iotaul && npm install --production && \
  echo "INFO: Cleaning unused software..." && \
  yum erase -y gcc-c++ gcc ppl cpp glibc-devel glibc-headers kernel-headers libgomp libstdc++-devel mpfr libss yum-utils libxml2-python git && \
  rm -rf /opt/node-v${NODEJS_VERSION}.tar.gz /opt/node-v${NODEJS_VERSION} && \
  # Erase without dependencies of the document formatting system (man). This cannot be removed using yum 
  # as yum uses hard dependencies and doing so will uninstall essential packages
  rpm -qa groff redhat-logos | xargs -r rpm -e --nodeps && \
  # Clean yum data
  yum clean all && rm -rf /var/lib/yum/yumdb && rm -rf /var/lib/yum/history && \
  # Rebuild rpm data files
  rpm -vv --rebuilddb && \
  # Delete unused locales. Only preserve en_US and the locale aliases
  find /usr/share/locale -mindepth 1 -maxdepth 1 ! -name 'en_US' ! -name 'locale.alias' | xargs -r rm -r && \
  bash -c 'localedef --list-archive | grep -v -e "en_US" | xargs localedef --delete-from-archive' && \
  # We use cp instead of mv as to refresh locale changes for ssh connections
  # We use /bin/cp instead of cp to avoid any alias substitution, which in some cases has been problematic
  /bin/cp -f /usr/lib/locale/locale-archive /usr/lib/locale/locale-archive.tmpl && \
  build-locale-archive && \
  find /opt/iotaul -name '.[^.]*' 2>/dev/null | xargs -r rm -rf && \
  # Clean npm cache
  npm cache clean && \
  # Don't need unused files inside docker images
  rm -rf /tmp/* /usr/local/lib/node_modules/npm/man /usr/local/lib/node_modules/npm/doc /usr/local/lib/node_modules/npm/html && \
  # We don't need to manage Linux account passwords requisites: lenght, mays/mins, etc
  # This cannot be removed using yum as yum uses hard dependencies and doing so will uninstall essential packages
  rm -rf /usr/share/cracklib && \
  # We don't need glibc locale data
  # This cannot be removed using yum as yum uses hard dependencies and doing so will uninstall essential packages
  rm -rf /usr/share/i18n /usr/{lib,lib64}/gconv && \
  # Don't need old log files inside docker images
  rm -f /var/log/*log

ENTRYPOINT bin/iotagent-ul config-blank.js

