FROM centos:7
LABEL maintainer="onwsk8r@gmail.com" \
      description="Prepare an environment for Python 3.4 with GDAL"

ENV ROOT_DIR=/python_gdal \
    GDAL_VERSION=2.2.1

WORKDIR $ROOT_DIR

# Create a virtualenv
RUN mkdir -p $ROOT_DIR/local && \
    yum -y install epel-release && \
    yum -y update && \
    yum -y install python34 python34-devel && \
    curl https://bootstrap.pypa.io/get-pip.py | python3.4 - && \
    pip install virtualenv

COPY --from=nowx/gdal_python:centos7-base-gdal2.2.1_05 $ROOT_DIR/local $ROOT_DIR/local
COPY --from=nowx/gdal_python:centos7-base-gdal2.2.1_05 /usr/bin/install_python_gdal.sh /sbin

# Install GDAL
RUN install_python_gdal.sh -b $ROOT_DIR/local/bin -d -p python3.4 -v $GDAL_VERSION /python_gdal/.venv
