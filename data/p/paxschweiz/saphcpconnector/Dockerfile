#
#  Copyright 2016 Pax, Schweizerische Lebensversicherungs-Gesellschaft AG
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

#
# SAP Hana Cloud Platform Connector as docker container (experimental)
# using centos - the open source red hat enterprise edition - fits with the needs of SAP HCP Connector
#

# source is red hat enterprise linux - open source implementation centos
FROM centos:7

MAINTAINER Martin Weber Nissle <martin.webernissle@pax.ch>

# Install dependencies and the SAP packages
RUN cd && \
    yum -y install initscripts which unzip wget && \
    wget --no-check-certificate --no-cookies --header "Cookie: eula_3.1_agreed=tools.hana.ondemand.com/developer-license-3.1.txt; path=/;" -S https://tools.hana.ondemand.com/additional/sapcc-2.9.0.2-linux-x64.zip && \
    unzip sapcc-2.9.0.2-linux-x64.zip && \
    wget --no-check-certificate --no-cookies --header "Cookie: eula_3.1_agreed=tools.hana.ondemand.com/developer-license-3.1.txt; path=/;" -S https://tools.hana.ondemand.com/additional/sapjvm-7.1.042-linux-x64.rpm && \
    rpm -i sapjvm-7.1.042-linux-x64.rpm && \
    rpm -i com.sap.scc-ui-2.9.0-7.x86_64.rpm

# Stop the service as it is started just after installation through rpm. Docker depends on a single foreground process - therefore the java process must be started directly and not through a service script.
RUN service scc_daemon stop
RUN cd /opt/sap/scc
RUN chsh -s /bin/bash sccadmin

# expose connector server
EXPOSE 8443
USER sccadmin
WORKDIR /opt/sap/scc

CMD /opt/sapjvm_7/bin/java -server -XtraceFile=log/vm_@PID_trace.log -XtraceFile=log/vm_@PID_trace.log -XX:+GCHistory -XX:GCHistoryFilename=log/vm_@PID_gc.prf -XX:+HeapDumpOnOutOfMemoryError -XX:+DisableExplicitGC -Xms1024m -Xmx1024m -XX:MaxNewSize=512m -XX:NewSize=512m -XX:+UseConcMarkSweepGC -XX:TargetSurvivorRatio=85 -XX:SurvivorRatio=6 -XX:MaxDirectMemorySize=2G -Dorg.apache.tomcat.util.digester.PROPERTY_SOURCE=com.sap.scc.tomcat.utils.PropertyDigester -Dosgi.requiredJavaVersion=1.6 -Dosgi.install.area=. -DuseNaming=osgi -Dorg.eclipse.equinox.simpleconfigurator.exclusiveInstallation=false -Dcom.sap.core.process=ljs_node -Declipse.ignoreApp=true -Dosgi.noShutdown=true -Dosgi.framework.activeThreadType=normal -Dosgi.embedded.cleanupOnSave=true -Dosgi.usesLimit=30 -Djava.awt.headless=true -Dio.netty.recycler.maxCapacity.default=256 -jar plugins/org.eclipse.equinox.launcher_1.1.0.v20100507.jar
#CMD ['/opt/sapjvm_7/bin/java', '-server', '-XtraceFile=log/vm_@PID_trace.log', '-XtraceFile=log/vm_@PID_trace.log', '-XX:+GCHistory', '-XX:GCHistoryFilename=log/vm_@PID_gc.prf', '-XX:+HeapDumpOnOutOfMemoryError', '-XX:+DisableExplicitGC', '-Xms1024m', '-Xmx1024m', '-XX:MaxNewSize=512m', '-XX:NewSize=512m', '-XX:+UseConcMarkSweepGC', '-XX:TargetSurvivorRatio=85', '-XX:SurvivorRatio=6', '-XX:MaxDirectMemorySize=2G', '-Dorg.apache.tomcat.util.digester.PROPERTY_SOURCE=com.sap.scc.tomcat.utils.PropertyDigester', '-Dosgi.requiredJavaVersion=1.6', '-Dosgi.install.area=.', '-DuseNaming=osgi', '-Dorg.eclipse.equinox.simpleconfigurator.exclusiveInstallation=false', '-Dcom.sap.core.process=ljs_node', '-Declipse.ignoreApp=true', '-Dosgi.noShutdown=true', '-Dosgi.framework.activeThreadType=normal', '-Dosgi.embedded.cleanupOnSave=true', '-Dosgi.usesLimit=30', '-Djava.awt.headless=true', '-Dio.netty.recycler.maxCapacity.default=256', '-jar plugins/org.eclipse.equinox.launcher_1.1.0.v20100507.jar']
