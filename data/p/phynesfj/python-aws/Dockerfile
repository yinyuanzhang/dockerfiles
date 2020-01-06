FROM python:2.7

MAINTAINER patrick.hynes@tds.fujitsu.com
# Update debian
RUN apt-get update && pip install --upgrade pip \
                && apt-get install -y jq \
                && pip install zip \
                && pip install --upgrade awscli \
                && pip install boto3 \
                && pip install slackclient \
                && pip install requests