FROM google/cloud-sdk:latest
MAINTAINER zulily <open-source@zulily.com>

# This image fixes some issues with Google's base cloud-sdk image, then installs some preview components

# Fix duplicate repository in /etc/apt/sources.list
RUN sed -i '/googleapis\.com wheezy main/d' /etc/apt/sources.list

# Install python-openssl and set up environment to enable it in gcloud
RUN apt-get update && apt-get install -y python-openssl
ENV CLOUDSDK_PYTHON_SITEPACKAGES 1

# Update gcloud components and install developer preview stuff
RUN gcloud components update preview
