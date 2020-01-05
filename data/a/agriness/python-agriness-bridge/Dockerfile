FROM python:3.6-slim

MAINTAINER Agriness

RUN apt-get update

RUN apt-get update && apt-get install -y curl zip python3-dev build-essential python3-dev python3-pip python3-cffi libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info jq libltdl7 git
RUN apt-get clean

RUN curl --insecure -OL https://github.com/SonarSource/sonar-scanner-cli/archive/3.2.0.1227.zip
RUN unzip 3.2.0.1227.zip
RUN rm 3.2.0.1227.zip

RUN pip install boto3 botocore awscli
