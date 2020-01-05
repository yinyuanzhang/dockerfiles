######################################################################################
# Step to build image from this docker file
# 
# 1: cd (change directoy) to this file
# 2: Make sure there is a asset directory in the directory
# 3: Run below command
#    - docker build -t <TAG_NAME> .
######################################################################################

FROM centos:7

LABEL Author="Base Information Management Private Limited" \
      Description="JRE 8u201 installed top of CentOS 7"


    # setting JAVA_HOME and JRE_HOME environment variables
ENV JAVA_HOME=/usr/java/jre1.8.0_201-amd64 \
    JRE_HOME=/usr/java/jre1.8.0_201-amd64 \
    # setting language relate environment variables
    LC_ALL=en_US.UTF-8 \
    LANG=en_US.UTF-8 \
    LANGUAGE=en_US.UTF-8

# update package repository
RUN yum install -y which file \
    && yum -y update

# copy jre 8 setup from local directory
COPY ./assets/jre-8u201-linux-x64.rpm /tmp/

    # install jre 8 using rpm
RUN rpm -i /tmp/jre-8u201-linux-x64.rpm \
    # remove jre setup
    && rm -f /tmp/jre-8u201-linux-x64.rpm \
    # configure time zone
    && echo IST > /etc/timezone

CMD [ "/bin/bash" ]
