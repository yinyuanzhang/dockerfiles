FROM johnpbatty/packer-gitlab-ci
MAINTAINER Telenium "github@telenium.ca"

# Install Required System Packages
RUN apk add --update alpine-sdk
RUN apk add py-pip
RUN apk add python-dev
RUN apk add linux-headers
RUN apk add libffi-dev
RUN apk add openssl-dev

# Install Required Python Packages
RUN pip install --upgrade pip
RUN pip install python-novaclient
RUN pip install python-glanceclient==0.12.0
