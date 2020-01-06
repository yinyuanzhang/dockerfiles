FROM ptolemy428/docker-troposphere:python-3
MAINTAINER Larry Liang <ptolemy428@gmail.com>

RUN apt-get update && apt-get install -y rsync

RUN pip install --no-cache-dir boto botocore boto3 \
                               ansible

WORKDIR /usr/src/app
