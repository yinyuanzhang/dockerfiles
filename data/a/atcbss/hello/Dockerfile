# LICENSE CDDL 1.0 + GPL 2.0

# Pull base image
# -------------------------------
FROM centos:7

# Maintainer
# -------------------------------
MAINTAINER Sergey Morgunov <smorgunov@at-consulting.ru>

# Set default password for root
# -------------------------------
RUN echo root:root | chpasswd

# Install additional packages
# -------------------------------
RUN yum -y --disableplugin=fastestmirror update && \
    yum -y --disableplugin=fastestmirror install unzip mc screen

COPY jdk-8u111-linux-x64.rpm /

# Install and configure Oracle JDK 7u79
# -------------------------------------
RUN rpm -i /jdk-8u111-linux-x64.rpm && \ 
    rm /jdk-8u111-linux-x64.rpm

ENV JAVA_HOME /usr/java/default
    
# Install unlimited JCE Policy for JDK8
# -------------------------------------
COPY jce_policy-8.zip /
RUN unzip jce_policy-8.zip && \
    mv /UnlimitedJCEPolicyJDK8/local_policy.jar $JAVA_HOME/jre/lib/security/ && \
    mv /UnlimitedJCEPolicyJDK8/US_export_policy.jar $JAVA_HOME/jre/lib/security/ && \
    rm /jce_policy-8.zip && \
    rm -rf /UnlimitedJCEPolicyJDK8

# Pull base image
# ---------------
FROM sonarqube

# Copy oracle jdbc driver
# -------------------------------------------------------------
COPY ojdbc6.jar $SONARQUBE_HOME/extensions/jdbc-driver/oracle/

# Define default command to start bash. 
CMD ["bash"]
