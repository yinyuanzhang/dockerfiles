######################################################################################
# Step to build image from this docker file
# 
# 1: cd (change directoy) to this file
# 2: Run below command
#    - docker build -t <TAG_NAME> .
######################################################################################

FROM centos:7

LABEL Author="Base Information Management Private Limited" \
      Description="Python 3.6 installed top of Cent OS 7"

    # setting language relate environment variables
ENV LC_ALL=en_US.UTF-8 \
    LANG=en_US.UTF-8 \
    LANGUAGE=en_US.UTF-8

RUN echo IST > /etc/timezone \
    && yum -y update \
    && yum -y install https://centos7.iuscommunity.org/ius-release.rpm \
    && yum -y install python36u python36u-libs python36u-devel python36u-pip \
    && yum -y install gcc gcc-c++ \
    && pip3.6 install virtualenv Cython

CMD [ "python3.6" ]
