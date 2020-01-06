FROM circleci/php:7.1-apache-jessie-node-browsers

# Add composer binary path.
ENV PATH="${PATH}:/home/circleci/.composer/vendor/bin"

# Install LibSSL and install system wide python tooling.  Ensure we are using
# python 3.
RUN sudo apt-get update
RUN sudo apt-get install -y --no-install-recommends apt-utils
RUN sudo apt-get install -y --no-install-recommends \
    libcurl4-openssl-dev \
    libssl-dev \
    python3-dev \
    python3-pip

# Cleanup from apt-get processing.
RUN sudo apt-get clean

# Install Requests and its associated OAuth2 library,
# which are used by the build script to perform Bitbucket
# API requests.  Also include pycurl, which may or may
# not be necessary in future releases.
RUN sudo pip3 install \
    pycurl \
    pyyaml \
    requests \
    requests_oauthlib

# Install the Drupal coder module.
RUN composer global require drupal/coder:~8.2.1 && \
    phpcs --config-set installed_paths /home/circleci/.composer/vendor/drupal/coder/coder_sniffer

# Replace python with python 3.  Run this LAST, as other programs
# (like yum) may depend on python.
RUN sudo rm -f /usr/bin/python && sudo ln -s /usr/bin/python3 /usr/bin/python
